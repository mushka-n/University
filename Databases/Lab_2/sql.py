sql_admin_functions = """

CREATE EXTENSION IF NOT EXISTS dblink;
CREATE OR REPLACE FUNCTION create_database() RETURNS void AS
$$
	BEGIN
		IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'hearthstone') THEN
			PERFORM dblink_exec('dbname=postgres user=postgres password=postgres', -- mmm...yammy
			'CREATE DATABASE hearthstone');
		END IF;
	END
$$
LANGUAGE plpgsql;


CREATE EXTENSION IF NOT EXISTS dblink;
CREATE OR REPLACE FUNCTION delete_database() RETURNS void AS
$$
	BEGIN
		PERFORM dblink_exec('dbname=postgres user=postgres password=postgres',
		'DROP DATABASE IF EXISTS hearthstone');
	END
$$
LANGUAGE plpgsql;



/* ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||    DB CREATION    ||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| */
"""

sql_functions  = """
CREATE OR REPLACE FUNCTION create_cards_info() RETURNS void AS
$$
	BEGIN
			CREATE TABLE IF NOT EXISTS "hscards"(
			id integer PRIMARY KEY,
			name text NOT NULL,
			rarity integer NOT NULL,
			manacost integer NOT NULL,
			description text NOT NULL,
			attack integer NOT NULL,
			health integer NOT NULL DEFAULT 0);

			CREATE INDEX on hscards(name);
	END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION create_fixes_info() RETURNS void AS
$$
	BEGIN
			CREATE TABLE IF NOT EXISTS event(
			id integer PRIMARY KEY,
			new_description text NOT NULL,
			card_id integer NOT NULL,
			gold_compensation integer NOT NULL);

			CREATE INDEX on event(new_description);

			CREATE TRIGGER new_description_handler
			AFTER INSERT ON
			event FOR EACH ROW EXECUTE PROCEDURE update_description();
	END
$$
LANGUAGE plpgsql;



/* ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||    CARDS    |||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| */



CREATE OR REPLACE FUNCTION get_cards()
RETURNS TABLE(id integer,
			  name text,
			  rarity integer,
			  manacost integer,
			  description text,
			  attack integer,
			  health integer)
AS
$func$
    BEGIN
        RETURN QUERY
        SELECT * FROM "hscards";
    END
$func$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION clear_cards()
RETURNS void AS
$$
    BEGIN
        DELETE FROM "hscards";
    END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION add_card(
              id integer,
			  name text,
			  rarity integer,
			  manacost integer,
			  description text,
			  attack integer,
			  health integer)
RETURNS void AS
$$
    BEGIN
        INSERT INTO "hscards" VALUES
        (id, nickname, battles_amount, average_damage, clan, tanks_amount, events_amount) ON CONFLICT DO NOTHING;
    END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION edit_card(
	          old_id integer,
			  new_name text,
			  new_rarity integer,
			  new_manacost integer,
			  new_description text,
			  new_attack integer,
			  new_health integer)
RETURNS void AS
$$
    BEGIN
        UPDATE "hscards"
        SET name = new_nickname,
            rarity = new_battles_amount,
            manacost = new_average_damage,
            description = new_clan,
            attack = new_tanks_amount,
            health = new_events_amount
        WHERE id = old_id;
    END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION find_card(nick_for_finding text)
RETURNS TABLE(id integer,
			  name text,
			  rarity integer,
			  manacost integer,
			  description text,
			  attack integer,
			  health integer)
AS
$func$
    BEGIN
        RETURN QUERY
        SELECT * FROM "hscards" WHERE name = nick_for_finding;
    END
$func$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION delete_card_by_name(nameToFind text)
RETURNS void AS
$$
    BEGIN
        DELETE FROM "hscards" WHERE name = nameToFind;
    END
$$
LANGUAGE plpgsql;



/* ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||    FIXES    |||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| */



CREATE OR REPLACE FUNCTION get_fixes()
RETURNS TABLE(id integer,
			  new_description text,
			  card_id integer,
			  gold_compensation integer)
AS
$func$
    BEGIN
        RETURN QUERY
        SELECT * FROM event;
    END
$func$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION clear_fixes()
RETURNS void AS
$$
    BEGIN
        DELETE FROM event;
    END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION add_fix(
              id integer,
			  new_description text,
			  card_id integer,
			  gold_compensation integer)
RETURNS void AS
$$
    BEGIN
        INSERT INTO event VALUES(id, new_description, card_id, gold_compensation) ON CONFLICT DO NOTHING;
    END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION edit_fix(
	          old_id integer,
			  new_event_name text,
			  new_event_prize integer,
			  new_account_id integer)
RETURNS void AS
$$
    BEGIN
        UPDATE event
        SET new_description = new_event_name,
            card_id = new_event_prize,
            gold_compensation = new_account_id
        WHERE id = old_id;
    END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION find_fix(event_name_for_finding text)
RETURNS TABLE(id integer,
			  new_description text,
			  card_id integer,
			  gold_compensation integer)
AS
$func$
    BEGIN
        RETURN QUERY
        SELECT * FROM event ev WHERE ev.new_description = event_name_for_finding;
    END
$func$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION delete_fix_by_name(name_for_finding text)
RETURNS void AS
$$
    BEGIN
        DELETE FROM event WHERE id = name_for_finding;
    END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION update_description() RETURNS TRIGGER AS
$$
    BEGIN
        IF TG_OP = 'INSERT' THEN
            UPDATE hscards SET events_amount = (
                SELECT description 
                FROM fixes 
                WHERE fixes.card_id = NEW.card_id) 
                    WHERE id = NEW.card_id;
            RETURN NEW;
        END IF;
    END;
$$
LANGUAGE plpgsql;

"""