/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50724
Source Host           : localhost:3306
Source Database       : zongce

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-08-08 15:24:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_credit
-- ----------------------------
DROP TABLE IF EXISTS `tb_credit`;
CREATE TABLE `tb_credit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(255) DEFAULT NULL COMMENT '科目',
  `credit` float(3,1) DEFAULT '4.0' COMMENT '学分',
  `term` int(2) DEFAULT '1' COMMENT '学期（1代表第一学期，2代表第二学期）',
  `enable_status` int(2) DEFAULT '1' COMMENT '1代表显示，0代表不显示',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_credit
-- ----------------------------
INSERT INTO `tb_credit` VALUES ('1', '无线射频识别技术与应用', '4.0', '1', '1');
INSERT INTO `tb_credit` VALUES ('2', '数字图像处理', '2.0', '1', '1');
INSERT INTO `tb_credit` VALUES ('3', '软件工程', '3.0', '1', '1');
INSERT INTO `tb_credit` VALUES ('4', 'Web应用开发', '3.0', '1', '1');
INSERT INTO `tb_credit` VALUES ('5', '嵌入式系统及应用', '4.0', '1', '1');
INSERT INTO `tb_credit` VALUES ('6', '嵌入式系统实训', '2.0', '1', '1');
INSERT INTO `tb_credit` VALUES ('7', '毛泽东思想和中国特色社会主义理论体系概论下', '3.0', '1', '1');
INSERT INTO `tb_credit` VALUES ('8', '移动终端开发技术', '3.0', '1', '1');
INSERT INTO `tb_credit` VALUES ('9', 'Web应用开发实训', '2.0', '2', '1');
INSERT INTO `tb_credit` VALUES ('10', 'ZigBee通信协议与应用', '4.0', '2', '1');
INSERT INTO `tb_credit` VALUES ('11', '专业英语', '2.0', '2', '1');
INSERT INTO `tb_credit` VALUES ('12', '信息安全技术', '3.0', '2', '1');
INSERT INTO `tb_credit` VALUES ('13', '无线传感器网络技术', '4.0', '2', '1');
