
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '用户的唯一标识符',
  `username` varchar(255) NOT NULL COMMENT '用户的用户名，必须唯一',
  `password` varchar(255) NOT NULL COMMENT '用户的密码，存储加密形式',
  `email` varchar(255) NOT NULL COMMENT '用户的电子邮箱地址',
  `is_del` tinyint DEFAULT '0' COMMENT '标记用户是否被删除，0为未删除，1为已删除',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '用户的创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='用户信息表'

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='产品信息表'

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='订单信息表'

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='订单详情表'



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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT '支付信息表';

CREATE TABLE `review` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '评论的唯一标识符',
  `order_id` int NOT NULL COMMENT '关联的订单ID',
  `rating` int NOT NULL COMMENT '用户给出的评分',
  `comment` text COMMENT '评论内容',
  `is_del` tinyint DEFAULT '0' COMMENT '标记评论是否被删除，0为未删除，1为已删除',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT '评论信息表';

