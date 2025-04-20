
-- Создание таблицы phonebook
create table if not exists phonebook (
    id serial primary key,
    first_name varchar,
    phone varchar
);

-- 1. Функция поиска по шаблону
create or replace function search_phonebook(pattern text)
returns table (id int, first_name varchar, phone varchar)
language plpgsql
as $$
begin
    return query
    select p.id, p.first_name, p.phone
    from phonebook p
    where p.first_name ilike '%' || pattern || '%'
       or p.phone ilike '%' || pattern || '%';
end;
$$;

-- 2. Процедура добавления/обновления пользователя
create or replace procedure insert_or_update_user(p_name varchar, p_phone varchar)
language plpgsql
as $$
begin
    if exists (select 1 from phonebook p where p.first_name = p_name) then
        update phonebook set phone = p_phone where first_name = p_name;
    else
        insert into phonebook (first_name, phone) values (p_name, p_phone);
    end if;
end;
$$;

-- 3. Процедура массовой вставки с проверкой номеров
create or replace procedure insert_many_users(names text[], phones text[], out incorrect_data text[])
language plpgsql
as $$
declare
    i int;
    phone_pattern text := '^\+?[0-9]{10,15}$';
begin
    incorrect_data := ARRAY[]::text[];
    for i in array_lower(names, 1)..array_upper(names, 1) loop
        if phones[i] ~ phone_pattern then
            call insert_or_update_user(names[i], phones[i]);
        else
            incorrect_data := array_append(incorrect_data, names[i] || ' - ' || phones[i]);
        end if;
    end loop;
end;
$$;

-- 4. Функция с пагинацией
create or replace function paginate_phonebook(p_limit int, p_offset int)
returns table (id int, first_name varchar, phone varchar)
language plpgsql
as $$
begin
    return query
    select p.id, p.first_name, p.phone
    from phonebook p
    order by p.id
    limit p_limit offset p_offset;
end;
$$;

-- 5. Процедура удаления по имени или номеру
create or replace procedure delete_from_phonebook(p_value text)
language plpgsql
as $$
begin
    delete from phonebook where first_name = p_value or phone = p_value;
end;
$$;
