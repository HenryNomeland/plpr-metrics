PRAGMA threads = 4;
CREATE OR REPLACE TABLE frames AS
SELECT #1, #2, COLUMNS('^Phoneme_')
FROM read_csv(".\testing.csv");
ALTER TABLE frames RENAME column00 TO frameID;
ALTER TABLE frames RENAME 'Phoneme_[UNK]' TO Phoneme_UNK;
ALTER TABLE frames RENAME 'Phoneme_[PAD]' TO Phoneme_PAD;
ALTER TABLE frames ADD COLUMN fileID INTEGER;
-- LIMIT 500
-- FROM read_csv("Z:\ASUTransfer\FullCorpus\distilled_w2tg_framewise_corpus.csv");
