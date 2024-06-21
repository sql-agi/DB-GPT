CREATE DATABASE IF NOT EXISTS qianfan CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

use qianfan;


CREATE TABLE IF NOT EXISTS `students` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '学生的唯一标识符',
    `first_name` VARCHAR(64) NOT NULL COMMENT '学生的名字',
    `last_name` VARCHAR(64) NOT NULL COMMENT '学生的姓氏',
    `gender` CHAR(1) NOT NULL COMMENT '性别 (M/F)',
    `date_of_birth` DATE NOT NULL COMMENT '出生日期',
    `address` VARCHAR(255) COMMENT '地址',
    `phone` VARCHAR(20) COMMENT '电话号码',
    `email` VARCHAR(128) COMMENT '电子邮箱',
    `enrollment_date` DATE NOT NULL COMMENT '入学日期',
    `is_del` TINYINT DEFAULT '0' COMMENT '标记记录是否被删除，0为未删除，1为已删除',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
    `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='学生信息表';

CREATE TABLE IF NOT EXISTS `teachers` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '教师的唯一标识符',
    `first_name` VARCHAR(64) NOT NULL COMMENT '教师的名字',
    `last_name` VARCHAR(64) NOT NULL COMMENT '教师的姓氏',
    `gender` CHAR(1) NOT NULL COMMENT '性别 (M/F)',
    `date_of_birth` DATE NOT NULL COMMENT '出生日期',
    `address` VARCHAR(255) COMMENT '地址',
    `phone` VARCHAR(20) COMMENT '电话号码',
    `email` VARCHAR(128) COMMENT '电子邮箱',
    `hire_date` DATE NOT NULL COMMENT '聘用日期',
    `is_del` TINYINT DEFAULT '0' COMMENT '标记记录是否被删除，0为未删除，1为已删除',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
    `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='教师信息表';

CREATE TABLE IF NOT EXISTS `courses` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '课程的唯一标识符',
    `course_name` VARCHAR(128) NOT NULL COMMENT '课程名称',
    `description` TEXT COMMENT '课程描述',
    `credits` INT NOT NULL COMMENT '学分',
    `is_del` TINYINT DEFAULT '0' COMMENT '标记记录是否被删除，0为未删除，1为已删除',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
    `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='课程信息表';


CREATE TABLE IF NOT EXISTS `course_schedule` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '课程安排的唯一标识符',
    `course_id` BIGINT UNSIGNED NOT NULL COMMENT '课程的唯一标识符',
    `teacher_id` BIGINT UNSIGNED NOT NULL COMMENT '教师的唯一标识符',
    `classroom` VARCHAR(64) NOT NULL COMMENT '教室',
    `schedule_time` DATETIME NOT NULL COMMENT '课程开始时间',
    `duration` INT UNSIGNED NOT NULL COMMENT '课程时长',
    `is_del` TINYINT DEFAULT '0' COMMENT '标记记录是否被删除，0为未删除，1为已删除',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
    `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
    PRIMARY KEY (`id`) USING BTREE,
    FOREIGN KEY (`course_id`) REFERENCES `courses`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`teacher_id`) REFERENCES `teachers`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='课程安排表';

CREATE TABLE IF NOT EXISTS `grades` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '成绩的唯一标识符',
    `student_id` BIGINT UNSIGNED NOT NULL COMMENT '学生的唯一标识符',
    `course_id` BIGINT UNSIGNED NOT NULL COMMENT '课程的唯一标识符',
    `grade` INT NOT NULL COMMENT '综合成绩',
    `regular_grades` INT NOT NULL COMMENT '平时成绩',
    `final_exam_scores` INT NOT NULL COMMENT '期末成绩',
    `date_recorded` DATE NOT NULL COMMENT '记录日期',
    `is_del` TINYINT DEFAULT '0' COMMENT '标记记录是否被删除，0为未删除，1为已删除',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
    `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
    PRIMARY KEY (`id`) USING BTREE,
    FOREIGN KEY (`student_id`) REFERENCES `students`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `courses`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='成绩记录表';



CREATE TABLE IF NOT EXISTS `exams` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '考试的唯一标识符',
    `course_id` BIGINT UNSIGNED NOT NULL COMMENT '课程的唯一标识符',
    `exam_date` DATETIME NOT NULL COMMENT '考试日期',
    `location` VARCHAR(64) NOT NULL COMMENT '考试地点',
    `is_del` TINYINT DEFAULT '0' COMMENT '标记记录是否被删除，0为未删除，1为已删除',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
    `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
    PRIMARY KEY (`id`) USING BTREE,
    FOREIGN KEY (`course_id`) REFERENCES `courses`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='考试安排表';

CREATE TABLE IF NOT EXISTS `exam_results` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '考试成绩的唯一标识符',
    `exam_id` BIGINT UNSIGNED NOT NULL COMMENT '考试的唯一标识符',
    `student_id` BIGINT UNSIGNED NOT NULL COMMENT '学生的唯一标识符',
    `score` DECIMAL(5, 2) NOT NULL COMMENT '考试分数',
    `is_del` TINYINT DEFAULT '0' COMMENT '标记记录是否被删除，0为未删除，1为已删除',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
    `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
    PRIMARY KEY (`id`) USING BTREE,
    FOREIGN KEY (`exam_id`) REFERENCES `exams`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`student_id`) REFERENCES `students`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='考试成绩表';

CREATE TABLE IF NOT EXISTS `classes` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '班级的唯一标识符',
    `class_name` VARCHAR(128) NOT NULL COMMENT '班级名称',
    `teacher_id` BIGINT UNSIGNED NOT NULL COMMENT '班主任的唯一标识符',
    `is_del` TINYINT DEFAULT '0' COMMENT '标记记录是否被删除，0为未删除，1为已删除',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
    `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
    PRIMARY KEY (`id`) USING BTREE,
    FOREIGN KEY (`teacher_id`) REFERENCES `teachers`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='班级信息表';


CREATE TABLE IF NOT EXISTS `student_classes` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '记录的唯一标识符',
    `student_id` BIGINT UNSIGNED NOT NULL COMMENT '学生的唯一标识符',
    `class_id` BIGINT UNSIGNED NOT NULL COMMENT '班级的唯一标识符',
    `is_del` TINYINT DEFAULT '0' COMMENT '标记记录是否被删除，0为未删除，1为已删除',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录的创建时间',
    `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录的最后更新时间',
    PRIMARY KEY (`id`) USING BTREE,
    FOREIGN KEY (`student_id`) REFERENCES `students`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`class_id`) REFERENCES `classes`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='学生班级关系表';


INSERT INTO `students` (`id`, `first_name`, `last_name`, `gender`, `date_of_birth`, `address`, `phone`, `email`, `enrollment_date`, `is_del`, `create_time`, `update_time`) VALUES
(1, '张', '伟', 'M', '2005-04-23', '北京市朝阳区光华路123号', '13800138000', 'zhangwei@example.com', '2020-09-01', 0, NOW(), NOW()),
(2, '王', '芳', 'F', '2006-08-15', '上海市徐汇区淮海中路456号', '13900139000', 'wangfang@example.com', '2020-09-01', 0, NOW(), NOW()),
(3, '李', '强', 'M', '2004-12-05', '广州市天河区天河路789号', '13700137000', 'liqiang@example.com', '2019-09-01', 0, NOW(), NOW()),
(4, '刘', '敏', 'F', '2005-02-20', '深圳市南山区南海大道321号', '13600136000', 'liumin@example.com', '2020-09-01', 0, NOW(), NOW()),
(5, '陈', '杰', 'M', '2006-11-30', '成都市武侯区锦绣路654号', '13500135000', 'chenjie@example.com', '2020-09-01', 0, NOW(), NOW()),
(6, '杨', '洋', 'F', '2005-07-17', '杭州市西湖区西湖路987号', '13400134000', 'yangyang@example.com', '2020-09-01', 0, NOW(), NOW()),
(7, '赵', '磊', 'M', '2004-05-12', '武汉市江汉区江汉路543号', '13300133000', 'zhaolei@example.com', '2019-09-01', 0, NOW(), NOW()),
(8, '周', '静', 'F', '2006-03-03', '南京市鼓楼区鼓楼路876号', '13200132000', 'zhoujing@example.com', '2020-09-01', 0, NOW(), NOW()),
(9, '吴', '强', 'M', '2005-09-25', '天津市和平区和平路111号', '13100131000', 'wuqiang@example.com', '2020-09-01', 0, NOW(), NOW()),
(10, '郑', '丽', 'F', '2006-06-18', '重庆市渝中区解放碑222号', '13000130000', 'zhengli@example.com', '2020-09-01', 0, NOW(), NOW());


INSERT INTO `teachers` (`id`, `first_name`, `last_name`, `gender`, `date_of_birth`, `address`, `phone`, `email`, `hire_date`, `is_del`, `create_time`, `update_time`) VALUES
(1, '王', '伟', 'M', '1980-01-10', '北京市朝阳区光华路123号', '13800138000', 'wangwei@example.com', '2010-09-01', 0, NOW(), NOW()),
(2, '李', '丽', 'F', '1985-02-15', '上海市徐汇区淮海中路456号', '13900139000', 'lili@example.com', '2012-09-01', 0, NOW(), NOW()),
(3, '张', '强', 'M', '1975-03-20', '广州市天河区天河路789号', '13700137000', 'zhangqiang@example.com', '2008-09-01', 0, NOW(), NOW()),
(4, '刘', '敏', 'F', '1982-04-25', '深圳市南山区南海大道321号', '13600136000', 'liumin@example.com', '2011-09-01', 0, NOW(), NOW()),
(5, '陈', '杰', 'M', '1978-05-30', '成都市武侯区锦绣路654号', '13500135000', 'chenjie@example.com', '2009-09-01', 0, NOW(), NOW()),
(6, '杨', '洋', 'F', '1983-06-05', '杭州市西湖区西湖路987号', '13400134000', 'yangyang@example.com', '2013-09-01', 0, NOW(), NOW()),
(7, '赵', '磊', 'M', '1976-07-10', '武汉市江汉区江汉路543号', '13300133000', 'zhaolei@example.com', '2007-09-01', 0, NOW(), NOW()),
(8, '周', '静', 'F', '1984-08-15', '南京市鼓楼区鼓楼路876号', '13200132000', 'zhoujing@example.com', '2014-09-01', 0, NOW(), NOW()),
(9, '吴', '强', 'M', '1979-09-20', '天津市和平区和平路111号', '13100131000', 'wuqiang@example.com', '2010-09-01', 0, NOW(), NOW()),
(10, '郑', '丽', 'F', '1981-10-25', '重庆市渝中区解放碑222号', '13000130000', 'zhengli@example.com', '2012-09-01', 0, NOW(), NOW());


INSERT INTO `courses` (`id`, `course_name`, `description`, `credits`, `is_del`, `create_time`, `update_time`) VALUES
(1, '数学', '基础数学课程', 3, 0, NOW(), NOW()),
(2, '语文', '基础语文课程', 3, 0, NOW(), NOW()),
(3, '英语', '基础英语课程', 3, 0, NOW(), NOW()),
(4, '物理', '基础物理课程', 4, 0, NOW(), NOW()),
(5, '化学', '基础化学课程', 4, 0, NOW(), NOW()),
(6, '生物', '基础生物课程', 3, 0, NOW(), NOW()),
(7, '历史', '基础历史课程', 2, 0, NOW(), NOW()),
(8, '地理', '基础地理课程', 2, 0, NOW(), NOW()),
(9, '政治', '基础政治课程', 2, 0, NOW(), NOW()),
(10, '体育', '基础体育课程', 1, 0, NOW(), NOW());


INSERT INTO `course_schedule` (`id`, `course_id`, `teacher_id`, `classroom`, `schedule_time`,`duration` ,`is_del`, `create_time`, `update_time`) VALUES
(1, 1, 1, 'A101', '2023-09-01 08:00:00',2, 0, NOW(), NOW()),
(2, 2, 2, 'B202', '2023-09-01 10:00:00',2, 0, NOW(), NOW()),
(3, 3, 3, 'C303', '2023-09-01 13:00:00',2, 0, NOW(), NOW()),
(4, 4, 4, 'D404', '2023-09-02 08:00:00',2, 0, NOW(), NOW()),
(5, 5, 5, 'E505', '2023-09-02 10:00:00',4, 0, NOW(), NOW()),
(6, 6, 6, 'F606', '2023-09-02 13:00:00',2, 0, NOW(), NOW()),
(7, 7, 7, 'G707', '2023-09-03 08:00:00',2, 0, NOW(), NOW()),
(8, 8, 8, 'H808', '2023-09-03 10:00:00',2, 0, NOW(), NOW()),
(9, 9, 9, 'I909', '2023-09-03 13:00:00',2, 0, NOW(), NOW()),
(10, 10, 10, 'J1010', '2023-09-04 08:00:00',2, 0, NOW(), NOW());


INSERT INTO `grades` (`id`, `student_id`, `course_id`, `grade`, `regular_grades`,`final_exam_scores`,`date_recorded`, `is_del`, `create_time`, `update_time`) VALUES
(1, 1, 1, 98,99,96, '2023-01-10', 0, NOW(), NOW()),
(2, 2, 2, 94,99,92, '2023-01-10', 0, NOW(), NOW()),
(3, 3, 3, 76,62,89, '2023-01-10', 0, NOW(), NOW()),
(4, 4, 4, 84,72,92, '2023-01-10', 0, NOW(), NOW()),
(5, 5, 5, 82,74,93, '2023-01-10', 0, NOW(), NOW()),
(6, 6, 6, 85,74,93, '2023-01-10', 0, NOW(), NOW()),
(7, 7, 7, 89,83,98, '2023-01-10', 0, NOW(), NOW()),
(8, 8, 8, 91,88,95, '2023-01-10', 0, NOW(), NOW()),
(9, 9, 9, 62,45,99, '2023-01-10', 0, NOW(), NOW()),
(10, 10, 10, 77,65,89, '2023-01-10', 0, NOW(), NOW());

INSERT INTO `exams` (`id`, `course_id`, `exam_date`, `location`, `is_del`, `create_time`, `update_time`) VALUES
(1, 1, '2023-12-01 09:00:00', 'A101', 0, NOW(), NOW()),
(2, 2, '2023-12-01 13:00:00', 'B202', 0, NOW(), NOW()),
(3, 3, '2023-12-02 09:00:00', 'C303', 0, NOW(), NOW()),
(4, 4, '2023-12-02 13:00:00', 'D404', 0, NOW(), NOW()),
(5, 5, '2023-12-03 09:00:00', 'E505', 0, NOW(), NOW()),
(6, 6, '2023-12-03 13:00:00', 'F606', 0, NOW(), NOW()),
(7, 7, '2023-12-04 09:00:00', 'G707', 0, NOW(), NOW()),
(8, 8, '2023-12-04 13:00:00', 'H808', 0, NOW(), NOW()),
(9, 9, '2023-12-05 09:00:00', 'I909', 0, NOW(), NOW()),
(10, 10, '2023-12-05 13:00:00', 'J1010', 0, NOW(), NOW());

INSERT INTO `exam_results` (`id`, `exam_id`, `student_id`, `score`, `is_del`, `create_time`, `update_time`) VALUES
(1, 1, 1, 95.5, 0, NOW(), NOW()),
(2, 2, 2, 88.0, 0, NOW(), NOW()),
(3, 3, 3, 92.0, 0, NOW(), NOW()),
(4, 4, 4, 75.0, 0, NOW(), NOW()),
(5, 5, 5, 85.0, 0, NOW(), NOW()),
(6, 6, 6, 90.0, 0, NOW(), NOW()),
(7, 7, 7, 78.5, 0, NOW(), NOW()),
(8, 8, 8, 82.0, 0, NOW(), NOW()),
(9, 9, 9, 89.0, 0, NOW(), NOW()),
(10, 10, 10, 87.0, 0, NOW(), NOW());


INSERT INTO `classes` (`id`, `class_name`, `teacher_id`, `is_del`, `create_time`, `update_time`) VALUES
(1, '初一一班', 1, 0, NOW(), NOW()),
(2, '初一二班', 2, 0, NOW(), NOW()),
(3, '初二一班', 3, 0, NOW(), NOW()),
(4, '初二二班', 4, 0, NOW(), NOW()),
(5, '初三一班', 5, 0, NOW(), NOW()),
(6, '初三二班', 6, 0, NOW(), NOW()),
(7, '初四一班', 7, 0, NOW(), NOW()),
(8, '初四二班', 8, 0, NOW(), NOW()),
(9, '初五一班', 9, 0, NOW(), NOW()),
(10, '初五二班', 10, 0, NOW(), NOW());



INSERT INTO `student_classes` (`id`, `student_id`, `class_id`, `is_del`, `create_time`, `update_time`) VALUES
(1, 1, 1, 0, NOW(), NOW()),
(2, 2, 2, 0, NOW(), NOW()),
(3, 3, 3, 0, NOW(), NOW()),
(4, 4, 4, 0, NOW(), NOW()),
(5, 5, 5, 0, NOW(), NOW()),
(6, 6, 6, 0, NOW(), NOW()),
(7, 7, 7, 0, NOW(), NOW()),
(8, 8, 8, 0, NOW(), NOW()),
(9, 9, 9, 0, NOW(), NOW()),
(10, 10, 10, 0, NOW(), NOW());

