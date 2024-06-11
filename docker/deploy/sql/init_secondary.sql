CREATE DATABASE IF NOT EXISTS shop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

use shop_db;


CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '用户的唯一标识符',
  `username` varchar(255) NOT NULL COMMENT '用户的用户名，必须唯一',
  `password` varchar(255) NOT NULL COMMENT '用户的密码，存储加密形式',
  `email` varchar(255) NOT NULL COMMENT '用户的电子邮箱地址',
  `is_del` tinyint DEFAULT '0' COMMENT '标记用户是否被删除，0为未删除，1为已删除',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '用户的创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户信息表';

CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '产品的唯一标识符',
  `product_name` varchar(255) NOT NULL COMMENT '产品名称',
  `description` text COMMENT '产品描述',
  `price` decimal(10,2) NOT NULL COMMENT '产品价格',
  `stock_quantity` int NOT NULL COMMENT '产品库存数量',
  `is_del` tinyint DEFAULT '0' COMMENT '标记产品是否被删除，0为未删除，1为已删除',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='产品信息表';

CREATE TABLE `order` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '订单的唯一标识符',
  `user_id` int NOT NULL COMMENT '下单的用户ID',
  `product_id` int NOT NULL COMMENT '订单中的产品ID',
  `quantity` int NOT NULL COMMENT '购买数量',
  `status` int NOT NULL COMMENT '订单状态（0-待支付，1-已支付，2-发货中，3-已完成，4-已取消）',
  `order_date` datetime NOT NULL COMMENT '订单生成的日期和时间',
  `is_del` tinyint DEFAULT '0' COMMENT '标记订单是否被删除，0为未删除，1为已删除',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订单信息表';

CREATE TABLE `order_details` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '订单详情的唯一标识符',
  `order_id` int NOT NULL COMMENT '关联的订单ID',
  `product_id` int NOT NULL COMMENT '关联的产品ID',
  `quantity` int NOT NULL COMMENT '购买数量',
  `unit_price` decimal(10,2) NOT NULL COMMENT '产品的单价',
  `subtotal` decimal(10,2) NOT NULL COMMENT '此项的总金额',
  `is_del` tinyint DEFAULT '0' COMMENT '标记订单详情是否被删除，0为未删除，1为已删除',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订单详情表';



CREATE TABLE `payment` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '支付信息的唯一标识符',
  `order_id` int NOT NULL COMMENT '关联的订单ID',
  `status` int NOT NULL COMMENT '支付状态（0-未支付，1-支付成功，2-支付失败，3-退款中，4-已退款）',
  `amount` decimal(10,2) NOT NULL COMMENT '支付金额',
  `payment_date` datetime NOT NULL COMMENT '支付日期',
  `is_del` tinyint DEFAULT '0' COMMENT '标记支付信息是否被删除，0为未删除，1为已删除',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '支付信息表';

CREATE TABLE `review` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '评论的唯一标识符',
  `order_id` int NOT NULL COMMENT '关联的订单ID',
  `rating` int NOT NULL COMMENT '用户给出的评分',
  `comment` text COMMENT '评论内容',
  `is_del` tinyint DEFAULT '0' COMMENT '标记评论是否被删除，0为未删除，1为已删除',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '评论信息表';

INSERT INTO `user` (username, password, email, is_del)
VALUES
('张三', 'password123', 'zhangsan@example.com', 0),
('李四', 'password123', 'lisi@example.com', 0),
('王五', 'password123', 'wangwu@example.com', 0),
('赵六', 'password123', 'zhaoliu@example.com', 0),
('钱七', 'password123', 'qianqi@example.com', 0),
('孙八', 'password123', 'sunba@example.com', 0),
('周九', 'password123', 'zhoujiu@example.com', 0),
('吴十', 'password123', 'wushi@example.com', 0),
('郑十一', 'password123', 'zhengshiyi@example.com', 0),
('冯十二', 'password123', 'fengshier@example.com', 0),
('陈十三', 'password123', 'chenshisan@example.com', 0),
('楚十四', 'password123', 'chushi@example.com', 0),
('卫十五', 'password123', 'weishiwu@example.com', 0),
('蒋十六', 'password123', 'jiangshiliu@example.com', 0),
('沈十七', 'password123', 'shenshiqi@example.com', 0),
('韩十八', 'password123', 'hanshiba@example.com', 0),
('杨十九', 'password123', 'yangshijiu@example.com', 0),
('朱二十', 'password123', 'zhuershi@example.com', 0),
('秦二一', 'password123', 'qineri@example.com', 0),
('尤二二', 'password123', 'youerer@example.com', 0);


INSERT INTO `product` (product_name, description, price, stock_quantity, is_del)
VALUES
('红茶', '传统的中国红茶', 10.00, 50, 0),
('绿茶', '绿茶清香四溢', 15.50, 40, 0),
('咖啡', '来自哥伦比亚的优质咖啡', 25.75, 30, 0),
('乌龙茶', '最好的乌龙茶叶', 12.00, 20, 0),
('普洱茶', '陈年的普洱', 30.00, 15, 0),
('黑咖啡', '纯正的黑咖啡', 22.00, 25, 0),
('拿铁', '香浓的拿铁', 20.00, 30, 0),
('卡布奇诺', '经典卡布奇诺', 18.50, 20, 0),
('白茶', '高级的白茶', 40.00, 10, 0),
('花茶', '花香四溢的花茶', 17.00, 25, 0);


INSERT INTO `order`
(id, user_id, product_id, quantity, status, order_date, is_del, create_time, update_time)
VALUES
(1, 1, 1, 2, 3, NOW(), 0, NOW(), NOW()),
(2, 2, 2, 1, 1, NOW(), 0, NOW(), NOW()),
(3, 3, 3, 3, 2, NOW(), 0, NOW(), NOW()),
(4, 4, 4, 1, 3, NOW(), 0, NOW(), NOW()),
(5, 5, 5, 5, 3, NOW(), 0, NOW(), NOW()),
(6, 6, 6, 2, 0, NOW(), 0, NOW(), NOW()),
(7, 7, 7, 1, 1, NOW(), 0, NOW(), NOW()),
(8, 8, 8, 3, 2, NOW(), 0, NOW(), NOW()),
(9, 9, 9, 1, 3, NOW(), 0, NOW(), NOW()),
(10, 10, 10, 2, 4, NOW(), 0, NOW(), NOW());


INSERT INTO `order_details` (order_id, product_id, quantity, unit_price, subtotal, is_del)
VALUES
(1, 1, 2, 10.00, 20.00, 0),
(2, 2, 1, 15.50, 15.50, 0),
(3, 3, 3, 25.75, 77.25, 0),
(4, 4, 1, 12.00, 12.00, 0),
(5, 5, 5, 30.00, 150.00, 0),
(6, 6, 2, 22.00, 44.00, 0),
(7, 7, 1, 20.00, 20.00, 0),
(8, 8, 3, 18.50, 55.50, 0),
(9, 9, 1, 40.00, 40.00, 0),
(10, 10, 2, 17.00, 34.00, 0);


INSERT INTO `payment` (order_id, status, amount, payment_date, is_del)
VALUES
(1, 1, 20.00, NOW(), 0),
(2, 1, 15.50, NOW(), 0),
(3, 2, 77.25, NOW(), 0),
(4, 1, 12.00, NOW(), 0),
(5, 1, 150.00, NOW(), 0),
(6, 0, 44.00, NOW(), 0),
(7, 1, 20.00, NOW(), 0),
(8, 2, 55.50, NOW(), 0),
(9, 1, 40.00, NOW(), 0),
(10, 1, 34.00, NOW(), 0);

INSERT INTO `review` (id, order_id, rating, comment, is_del, create_time, update_time)
VALUES
(1, 1, 5, '非常好的红茶', 0, NOW(), NOW()),
(2, 2, 4, '很清新的绿茶', 0, NOW(), NOW()),
(3, 3, 3, '咖啡味道不错', 0, NOW(), NOW()),
(4, 4, 5, '乌龙茶香气浓郁', 0, NOW(), NOW()),
(5, 5, 5, '普洱味道深厚', 0, NOW(), NOW()),
(6, 6, 4, '黑咖啡很纯', 0, NOW(), NOW()),
(7, 7, 5, '拿铁非常香', 0, NOW(), NOW()),
(8, 8, 4, '卡布奇诺味道好', 0, NOW(), NOW()),
(9, 9, 5, '白茶非常好喝', 0, NOW(), NOW()),
(10, 10, 4, '花茶的香味很舒服', 0, NOW(), NOW()),
(11, 1, 4, '还会再买的', 0, NOW(), NOW()),
(12, 2, 4, '满意', 0, NOW(), NOW()),
(13, 3, 5, '三次购买了', 0, NOW(), NOW()),
(14, 4, 5, '推荐给朋友了', 0, NOW(), NOW()),
(15, 5, 4, '价格有点贵', 0, NOW(), NOW()),
(16, 6, 4, '比预想的好', 0, NOW(), NOW()),
(17, 7, 5, '味道一级棒', 0, NOW(), NOW()),
(18, 8, 1, '不太好', 0, NOW(), NOW()),
(19, 9, 2, '凑合', 0, NOW(), NOW()),
(20, 10, 4, '会再次购买', 0, NOW(), NOW());



