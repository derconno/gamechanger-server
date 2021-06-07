# GameChanger Server

Das Backend für die GameChanger App. 

## API Endpoints

### GET /game/\<id\>

| Key | Value |
| --- | --- |
| \<id\> | ID des Spiels |
| Request Data | None |
| Response Data | `{"gametype": GAMETYPE, "lastUpdate": TIMESTAMP}` |

### GET /game/\<id\>/data

| Key | Value |
| --- | --- |
| \<id\> | ID des Spiels |
| Request Data | None |
| Response Data | `{"Points": {"PLAYER": [NR, NR, NR, ...], ...}, "Calls": {...}, "allowUpdates": BOOL}` |

### PUT /game

| Key | Value |
| --- | --- |
| Request Data | `{"gametype": GAMETYPE, "Players": [PLAYER1, PLAYER2, ...]}` |
| Response Data | `{"id": ID}` |

### POST /game/\<id\>

| Key | Value |
| --- | --- |
| \<id\> | ID des Spiels |
| Request Data | `{"Points": {"PLAYER": [NR, NR, NR, ...], ...}, "Calls": {...}}` |
| Response Data | None |