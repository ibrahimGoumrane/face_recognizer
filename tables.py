import mysql.connector as sq
from mysql.connector import errorcode



class Tables:
    TABLES = {}
    table_number=len(TABLES.keys())
    table_names=TABLES.keys()
    
    TABLES['class'] = (
        "CREATE TABLE IF NOT EXISTS `class` ("
        "  `class_id` INT NOT NULL AUTO_INCREMENT,"
        "  `cycle` TEXT NOT NULL,"
        "  `cycle_year` INT NOT NULL,"
        "  `filiere` TEXT NOT NULL,"
        "  PRIMARY KEY (`class_id`)"
        ")"
    )
    TABLES['teachers'] = (
        "CREATE TABLE IF NOT EXISTS `teachers` ("
        "  `teacher_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
        "  `teacher_name` TEXT NOT NULL"
        ")"
    )
    TABLES['students'] = (
        "CREATE TABLE IF NOT EXISTS `students` ("
        "  `student_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
        "  `student_name` TEXT NOT NULL,"
        "  `class_id` INT NOT NULL,"
        "  CONSTRAINT `students_class_id` FOREIGN KEY (`class_id`) "
        "     REFERENCES `class` (`class_id`) ON DELETE CASCADE"
        ")"
    )
    TABLES['module'] = (
        "CREATE TABLE IF NOT EXISTS `module` ("
        "  `module_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
        "  `class_id` INT NOT NULL,"
        "  `teacher_id` INT NOT NULL,"
        "  `module_name` TEXT NOT NULL,"
        "  CONSTRAINT `module_class_id` FOREIGN KEY (`class_id`) "
        "     REFERENCES `class` (`class_id`) ON DELETE CASCADE,"
        "  CONSTRAINT `module_teacher_id` FOREIGN KEY (`teacher_id`) "
        "     REFERENCES `teachers` (`teacher_id`) ON DELETE CASCADE"
        ")"
    )
    
    TABLES['seance'] = (
        "CREATE TABLE IF NOT EXISTS `seance` ("
        "  `seance_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
        "  `class_id` INT NOT NULL,"
        "  `module_id` INT NOT NULL,"
        "  `start_hour` INT NOT NULL,"
        "  `end_hour` INT NOT NULL,"
        "  `week_day` VARCHAR(10) NOT NULL,"
        "  `full_date` DATE NOT NULL,"
        "  CONSTRAINT `seance_class_id` FOREIGN KEY (`class_id`) "
        "     REFERENCES `class` (`class_id`) ON DELETE CASCADE,"
        "  CONSTRAINT `seance_module_id` FOREIGN KEY (`module_id`) "
        "     REFERENCES `module` (`module_id`) ON DELETE CASCADE"
        ")"
    )

    TABLES['presence'] = (
        "CREATE TABLE IF NOT EXISTS `presence` ("
        "  `presence_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
        "  `seance_id` INT NOT NULL,"
        "  `student_id` INT NOT NULL,"
        "  `state` BOOLEAN  NOT NULL DEFAULT FALSE,"
        "  CONSTRAINT `presence_seance_id` FOREIGN KEY (`seance_id`) "
        "     REFERENCES `seance` (`seance_id`) ON DELETE CASCADE,"
        "  CONSTRAINT `presence_student_id` FOREIGN KEY (`student_id`) "
        "     REFERENCES `students` (`student_id`) ON DELETE CASCADE"
        ")"
    )

