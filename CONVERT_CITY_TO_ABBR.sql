USE `x5t20wxo8nmqqxfz`;

ALTER TABLE `humidity`
CHANGE COLUMN `Vancouver`	`van` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Portland`    `por` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `SanFrancisco`	`sfran` TEXT NULL DEFAULT NULL , 
CHANGE COLUMN `Seattle`	`sea` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `LosAngeles`	`la` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `SanDiego`	`sand` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `LasVegas`	`laveg` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Phoenix`	`pho` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Albuquerque`	`alb` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Denver`	`den` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `SanAntonio`	`sant` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Dallas`	`dal` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Houston`	`hou` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `KansasCity`	`ksc` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Minneapolis`	`min` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `SaintLouis`	`stlo` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Chicago`	`chi` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Nashville`	`nash` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Indianapolis`	`ind` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Atlanta`	`atl` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Detroit`	`det` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Jacksonville`	`jac` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Charlotte`	`char` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Miami`	`mai` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Pittsburgh`	`pit` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Toronto`	`tor` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Philadelphia`	`phi` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `NewYork`	`nyc` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Montreal`	`mon` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Boston`	`bos` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Beersheba`	`bee` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `TelAviv`	`tel` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Eilat`	`eil` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Haifa`	`hai` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Nahariyya`	`nah` TEXT NULL DEFAULT NULL ,
CHANGE COLUMN `Jerusalem`	`jer` TEXT NULL DEFAULT NULL;