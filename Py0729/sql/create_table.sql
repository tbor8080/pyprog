CREATE TABLE 'COMMODITY_LIST'(
    'commodity_id' INTEGER NOT NULL,
    'comp_id' INTEGER,
    'commodity_name' TEXT NOT NULL,
    'commodity_maker' TEXT,
    'commodity_word' TEXT,
    'stock' INTEGER NOT NULL,
    'remark' TEXT,
    PRIMARY KEY('product_id', AUTOINCREMENT)
);
CREATE TABLE 'COMPANY_INFO' (
    'comp_id' INTEGER NOT NULL,  
    'comp_name_ja' TEXT NOT NULL,
    'comp_name_en' TEXT NOT NULL,
    'comp_description' TEXT,
    'comp_register' DATE,
    PRIMARY KEY('comp_id' AUTOINCREMENT)
);
CREATE TABLE 'COMPANY_DOCUMENT_LIST' (
    'document_num' INTEGER NOT NULL,
    'comp_id' INTEGER NOT NULL,
    'category' TEXT,
    'document_name' TEXT,
    'company_deploy' TEXT,
    'from_save_date' DATE,
    'disposal_date' DATE,
    'remarks' TEXT,
    PRIMARY KEY('document_num' AUTOINCREMENT)
);

# 
SELECT NAME FROM sqlite_master WHERE TYPE='table';

SELECT * FROM  WHERE name LIKE '%{word}';
