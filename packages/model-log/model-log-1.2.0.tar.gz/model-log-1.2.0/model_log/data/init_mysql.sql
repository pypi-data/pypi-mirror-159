drop table if exists project;
drop table if exists sub_model;
drop table if exists model_param;
drop table if exists model_metric;
drop table if exists best_result;
create table project
(
    project_id integer auto_increment primary key,
    project_name   varchar(500)     not null,
    project_remark varchar(500),
    nick_name      varchar(100),
    create_time    datetime not null,
    del_flag       INTEGER default 0 not null
);
create index project_create_time_index
    on project (create_time);
create index project_del_flag_index
    on project (del_flag);
create index project_nick_name_index
    on project (nick_name);
create table model_metric
(
    metric_id integer auto_increment primary key,
    sub_model_id INTEGER  not null,
    metric_name  varchar(100)     not null,
    metric_type  varchar(100)     not null,
    epoch        INTEGER  not null,
    metric_value float    not null,
    create_time  datetime not null
);
create index model_metric_create_time_index
    on model_metric (create_time);
create index model_metric_epoch_index
    on model_metric (epoch);
create index model_metric_metric_name_index
    on model_metric (metric_name);
create index model_metric_metric_type_index
    on model_metric (metric_type);
create index model_metric_metric_value_index
    on model_metric (metric_value);
create index model_metric_sub_model_id_index
    on model_metric (sub_model_id);
create table model_param
(
    param_id integer auto_increment primary key,
    sub_model_id INTEGER  not null,
    param_type   varchar(100)     not null,
    param_name   varchar(100)     not null,
    param_value  varchar(100)     not null,
    create_time  datetime not null
);
create index model_param_create_time_index
    on model_param (create_time);
create index model_param_param_name_index
    on model_param (param_name);
create index model_param_param_type_index
    on model_param (param_type);
create index model_param_param_value_index
    on model_param (param_value);
create index model_param_sub_model_id_index
    on model_param (sub_model_id);
create table sub_model
(
    sub_model_id integer auto_increment primary key,
    project_id         INTEGER  not null,
    sub_model_sequence INTEGER  not null,
    sub_model_name     varchar(500)     not null,
    sub_model_remark   varchar(500),
    nick_name          varchar(100),
    create_time        datetime not null,
    del_flag           INTEGER default 0 not null,
    is_finish          int
);
create index sub_model_create_time_index
    on sub_model (create_time);
create index sub_model_del_flag_index
    on sub_model (del_flag);
create index sub_model_is_finish_index
    on sub_model (is_finish);
create index sub_model_nick_name_index
    on sub_model (nick_name);
create index sub_model_project_id_index
    on sub_model (project_id);
create index sub_model_sub_model_sequence_index
    on sub_model (sub_model_sequence);
create table best_result
(
    best_result_id integer auto_increment primary key,
    sub_model_id   integer  not null,
    best_name      varchar(100)     not null,
    best_value     float    not null,
    best_epoch     INTEGER  not null,
    create_time    datetime not null
);
create index best_result_best_epoch_index
    on best_result (best_epoch);
create index best_result_best_name_index
    on best_result (best_name);
create index best_result_best_value_index
    on best_result (best_value);
create index best_result_create_time_index
    on best_result (create_time);
create index best_result_sub_model_id_index
    on best_result (sub_model_id);