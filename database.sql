-- 删除旧表
DROP TABLE IF EXISTS conversions;

-- 新建表结构
CREATE TABLE conversions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    source_code TEXT NOT NULL,
    detected_lang VARCHAR(50) NOT NULL,  -- 自动检测的语言
    target_lang VARCHAR(50) NOT NULL,
    converted_code TEXT,
    conversion_date DATETIME NOT NULL
);