CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM contacts WHERE phone = p_phone
    ) THEN
        RAISE NOTICE 'Phone number % already exists, skipping insert/update', p_phone;
    ELSE
        IF EXISTS (
            SELECT 1 FROM contacts WHERE name = p_name
        ) THEN
            UPDATE contacts
            SET phone = p_phone
            WHERE name = p_name;
        ELSE
            INSERT INTO contacts(name, phone)
            VALUES (p_name, p_phone);
        END IF;
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE bulk_upsert_contacts(
    p_names TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_names, 1)
    LOOP
        IF p_phones[i] ~ '^[0-9]+$' THEN
            IF EXISTS (SELECT 1 FROM contacts WHERE phone = p_phones[i]) THEN
                RAISE NOTICE 'Phone number % already exists, skipping %', p_phones[i], p_names[i];
            ELSE
                IF EXISTS (SELECT 1 FROM contacts WHERE name = p_names[i]) THEN
                    UPDATE contacts
                    SET phone = p_phones[i]
                    WHERE name = p_names[i];
                ELSE
                    INSERT INTO contacts(name, phone)
                    VALUES (p_names[i], p_phones[i]);
                END IF;
            END IF;
        ELSE
            RAISE NOTICE 'Invalid phone for %: %', p_names[i], p_phones[i];
        END IF;
    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact_proc(
    p_value TEXT,
    p_type TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_type = 'name' THEN
        DELETE FROM contacts WHERE name = p_value;
    ELSIF p_type = 'phone' THEN
        DELETE FROM contacts WHERE phone = p_value;
    ELSE
        RAISE NOTICE 'Invalid delete type';
    END IF;
END;
$$;