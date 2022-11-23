create table day(
    id  integer primary key autoincrement not null,
    day text
);

create table anime(
    id              integer primary key autoincrement not null,
    day             text not null references day(day),
    anime           text,
    episode_count   integer not null,
    active          boolean not null
);