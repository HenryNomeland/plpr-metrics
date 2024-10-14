PRAGMA threads = 4;

-- Creates the table and columns that are necessary - local indices are unique within model-aligner pairs - other indicies are unique for every row/value
-- Inserts the Wav2TextGrid/KaldiDistilled pair
CREATE OR REPLACE TABLE Frames AS
    SELECT 'Wav2TextGrid' AS Aligner, 
           'Charsiu' AS AcousticModel, 
           FileName,
           FrameNum,
           ExpectedPhonemeProb, 
           Phone AS ExpectedPhoneme,
           COLUMNS('^Phoneme_'), 
           ROW_NUMBER() OVER() AS LocalFrameID, 
           DENSE_RANK() OVER(ORDER BY FileName) AS LocalFileID
    FROM read_csv("Z:\ASUTransfer\FullCorpus\charsiu_w2tg_framewise_corpus.csv");
ALTER TABLE Frames RENAME 'Phoneme_[UNK]' TO Phoneme_UNK;
ALTER TABLE Frames RENAME 'Phoneme_[PAD]' TO Phoneme_PAD;

-- Inserts the MFA/KaldiDistilled Pair
-- INSERT INTO Frames
--     SELECT 'MFA' AS Aligner, 
--            'Charsiu' AS AcousticModel, 
--            FileName,
--            FrameNum, 
--            ExpectedPhonemeProb,
--            ExpectedPhoneme,
--            COLUMNS('^Phoneme_'), 
--            ROW_NUMBER() OVER() AS LocalFrameID, 
--            DENSE_RANK() OVER(ORDER BY FileName) AS LocalFileID
--     FROM read_csv("Z:\ASUTransfer\FullCorpus\charsiu_mfa_framewise_corpus.csv");

-- Figures out the global indicies from the local indicies and adds those columns
CREATE OR REPLACE TABLE Frames AS
    SELECT *
    FROM Frames
    ORDER BY Aligner, AcousticModel, FileName, FrameNum;
ALTER TABLE Frames ADD COLUMN FrameID INTEGER;
WITH RankedFrames AS (
        SELECT ROW_NUMBER() OVER() AS FrameID, f.*
        FROM Frames f
    )
    UPDATE Frames
        SET FrameID = RankedFrames.FrameID
        FROM RankedFrames
        WHERE Frames.FileName = RankedFrames.FileName AND Frames.AcousticModel = RankedFrames.AcousticModel AND Frames.Aligner = RankedFrames.Aligner AND Frames.LocalFrameID = RankedFrames.LocalFrameID AND Frames.FrameNum = RankedFrames.FrameNum;
ALTER TABLE Frames ADD COLUMN FileID INTEGER;
WITH RankedFiles AS (
        SELECT DENSE_RANK() OVER(ORDER BY Aligner, AcousticModel, FileName) AS FileID, f.*
        FROM Frames f
    )
    UPDATE Frames
        SET FileID = RankedFiles.FileID
        FROM RankedFiles
        WHERE Frames.FileName = RankedFiles.FileName AND Frames.AcousticModel = RankedFiles.AcousticModel AND Frames.Aligner = RankedFiles.Aligner AND Frames.LocalFileID = RankedFiles.LocalFileID AND Frames.FrameNum = RankedFiles.FrameNum;

--Testing Table for Command Line Printouts
CREATE OR REPLACE TABLE testing AS
SELECT DISTINCT ExpectedPhoneme, FrameID, FileName FROM Frames
ORDER BY FrameID;

--Unpivoting everything to get out of wide format and into long format and making a new table for measurements 
CREATE OR REPLACE TABLE Measurements AS
    SELECT Aligner,
           AcousticModel, 
           FileName,
           FileID,
           FrameID,
           REPLACE(MeasuredPhoneme, 'Phoneme_', '') AS MeasuredPhoneme,
           Probability
    FROM Frames
    UNPIVOT(
        Probability FOR MeasuredPhoneme IN (COLUMNS('^Phoneme_'))
    );
ALTER TABLE Measurements ADD COLUMN MeasurementID INTEGER;
WITH RankedMeasurements AS (
        SELECT ROW_NUMBER() OVER() AS MeasurementID, m.*
        FROM Measurements m
    )
    UPDATE Measurements
        SET MeasurementID = RankedMeasurements.MeasurementID
        FROM RankedMeasurements
        WHERE Measurements.MeasuredPhoneme = RankedMeasurements.MeasuredPhoneme AND Measurements.FrameID = RankedMeasurements.FrameID; 

--Remaking the frames table to be more of a summary of statistics for that frame
CREATE OR REPLACE TABLE Frames AS
    SELECT Aligner, 
           AcousticModel,
           FileName,
           f.FrameID,
           FileID,
           ExpectedPhonemeProb,
           ExpectedPhoneme,
           m.MostLikelyPhonemeProb
    FROM Frames f
    JOIN (
        SELECT FrameID, MAX(Probability) AS MostLikelyPhonemeProb
        FROM Measurements
        GROUP BY FrameID
    ) m ON f.FrameID = m.FrameID
    ORDER BY f.FrameID;
ALTER TABLE Frames ADD COLUMN MostLikelyPhoneme TEXT;
UPDATE Frames f 
    SET MostLikelyPhoneme = x.MeasuredPhoneme
    FROM (
        SELECT m.FrameID, m.MeasuredPhoneme
        FROM Measurements m
        JOIN (
            SELECT FrameID, MAX(Probability) AS MaxValue
            FROM Measurements
            GROUP BY FrameID
        ) maxvalues ON m.FrameID = maxvalues.FrameID AND m.Probability = maxvalues.MaxValue
    ) AS x
    WHERE f.FrameID = x.FrameID;


-- --Makes new tables identical to the old tables except we recalculate EVERYTHING with schwa being dropped entirely
-- CREATE OR REPLACE TABLE MeasurementsNoSchwa AS
--     SELECT Measurements.*, f.ExpectedPhoneme
--     FROM Measurements
--     JOIN (
--         SELECT FrameID, ExpectedPhoneme
--         FROM Frames
--     ) f ON Measurements.FrameID = f.FrameID;
-- DELETE FROM MeasurementsNoSchwa WHERE ExpectedPhoneme = 'AH';
-- DELETE FROM MeasurementsNoSchwa WHERE MeasuredPhoneme = 'AH';
-- --At some point I need to write the code which redistributes the probability mass
-- CREATE OR REPLACE TABLE MeasurementsNoSchwa AS
--     SELECT Aligner, AcousticModel, FileName, FileID, FrameID, MeasuredPhoneme, Probability, MeasurementID
--     FROM MeasurementsNoSchwa;
-- CREATE OR REPLACE TABLE FramesNoSchwa AS
--     SELECT Aligner, 
--            AcousticModel,
--            FileName,
--            f.FrameID,
--            FileID,
--            ExpectedPhonemeProb,
--            ExpectedPhoneme,
--            m.MostLikelyPhonemeProb
--     FROM Frames f
--     JOIN (
--         SELECT FrameID, MAX(Probability) AS MostLikelyPhonemeProb
--         FROM MeasurementsNoSchwa
--         GROUP BY FrameID
--     ) m ON f.FrameID = m.FrameID
--     ORDER BY f.FrameID;
-- ALTER TABLE FramesNoSchwa ADD COLUMN MostLikelyPhoneme TEXT;
-- UPDATE FramesNoSchwa f 
--     SET MostLikelyPhoneme = x.MeasuredPhoneme
--     FROM (
--         SELECT m.FrameID, m.MeasuredPhoneme
--         FROM MeasurementsNoSchwa m
--         JOIN (
--             SELECT FrameID, MAX(Probability) AS MaxValue
--             FROM MeasurementsNoSchwa
--             GROUP BY FrameID
--         ) maxvalues ON m.FrameID = maxvalues.FrameID AND m.Probability = maxvalues.MaxValue
--     ) AS x
--     WHERE f.FrameID = x.FrameID;
-- UPDATE FramesNoSchwa
--     SET ExpectedPhonemeProb = (
--         SELECT m.Probability
--         FROM MeasurementsNoSchwa m 
--         WHERE m.FrameID = FramesNoSchwa.FrameID AND m.MeasuredPhoneme = FramesNoSchwa.ExpectedPhoneme
--     )