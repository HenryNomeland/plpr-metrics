PRAGMA threads = 4;

--Gets all of the 2-9 year old samples from the Wav2TG KaldiDistilled NoSchwa set and outputs them
COPY (
    SELECT *
    FROM Frames
    WHERE SUBSTR(FileName, 4, 1) = '2' AND Aligner = 'Wav2TextGrid' AND AcousticModel = 'Charsiu'
) TO '.\2yo_table.csv' (HEADER, DELIMITER ',');
COPY (
    SELECT *
    FROM Frames
    WHERE SUBSTR(FileName, 4, 1) = '3' AND Aligner = 'Wav2TextGrid' AND AcousticModel = 'Charsiu'
) TO '.\3yo_table.csv' (HEADER, DELIMITER ',');
COPY (
    SELECT *
    FROM Frames
    WHERE SUBSTR(FileName, 4, 1) = '4' AND Aligner = 'Wav2TextGrid' AND AcousticModel = 'Charsiu'
) TO '.\4yo_table.csv' (HEADER, DELIMITER ',');
COPY (
    SELECT *
    FROM Frames
    WHERE SUBSTR(FileName, 4, 1) = '5' AND Aligner = 'Wav2TextGrid' AND AcousticModel = 'Charsiu'
) TO '.\5yo_table.csv' (HEADER, DELIMITER ',');
COPY (
    SELECT *
    FROM Frames
    WHERE SUBSTR(FileName, 4, 1) = '6' AND Aligner = 'Wav2TextGrid' AND AcousticModel = 'Charsiu'
) TO '.\6yo_table.csv' (HEADER, DELIMITER ',');
COPY (
    SELECT *
    FROM Frames
    WHERE SUBSTR(FileName, 4, 1) = '7' AND Aligner = 'Wav2TextGrid' AND AcousticModel = 'Charsiu'
) TO '.\7yo_table.csv' (HEADER, DELIMITER ',');
COPY (
    SELECT *
    FROM Frames
    WHERE SUBSTR(FileName, 4, 1) = '8' AND Aligner = 'Wav2TextGrid' AND AcousticModel = 'Charsiu'
) TO '.\8yo_table.csv' (HEADER, DELIMITER ',');
COPY (
    SELECT *
    FROM Frames
    WHERE SUBSTR(FileName, 4, 1) = '9' AND Aligner = 'Wav2TextGrid' AND AcousticModel = 'Charsiu'
) TO '.\9yo_table.csv' (HEADER, DELIMITER ',');