BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY,username text,           email text,phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Kim','kim@naver.com','000-0000-0000','kim.com','2023-12-12 14:54:26');
INSERT INTO "users" VALUES(2,'Park','park@daum.net','010-0000-0000','park.com','2023-12-12 14:54:26');
INSERT INTO "users" VALUES(3,'lee','lee@daum.net','010-0000-0000','lee.com','2023-12-12 14:54:26');
INSERT INTO "users" VALUES(4,'cho','cho@daum.net','010-0000-0000','cho.com','2023-12-12 14:54:26');
INSERT INTO "users" VALUES(5,'choi','choi@daum.net','010-0000-0000','choi.com','2023-12-12 14:54:26');
COMMIT;
