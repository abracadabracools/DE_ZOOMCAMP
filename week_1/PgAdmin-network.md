## 🐳 Command Breakdown

`docker run -it \     -e POSTGRES_USER="root" \     -e POSTGRES_PASSWORD="root" \     -e POSTGRES_DB="ny_taxi" \     -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \     -p 5432:5432 \     --network=pg-network \     --name pg-database \     postgres:13`

* * *

### 🔹 1. `docker run -it`

*   `docker run` → Starts a new container from a Docker image.
    
*   `-it` → Interactive + terminal mode (lets you see logs and interact if needed).
    

* * *

### 🔹 2. Environment Variables: `-e`

These set up the **initial database configuration** inside the container:

*   `-e POSTGRES_USER="root"` → Creates a PostgreSQL user named `root`.
    
*   `-e POSTGRES_PASSWORD="root"` → Sets that user’s password to `root`.
    
*   `-e POSTGRES_DB="ny_taxi"` → Creates a new database named `ny_taxi` on startup.
    

✅ Result: When the container runs, PostgreSQL will start with:

*   A user: `root`
    
*   A password: `root`
    
*   A database: `ny_taxi`
    

* * *

### 🔹 3. Volume Mount: `-v`

`-v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data`

*   `-v` → Mounts a folder on your **host machine** into the **container**.
    
*   `$(pwd)/ny_taxi_postgres_data` → The folder on your **local machine** (in the current directory).
    
*   `/var/lib/postgresql/data` → The location **inside the container** where PostgreSQL stores its database files.
    

✅ Why this is important:

*   Without this, **all your data disappears** when the container stops.
    
*   With this, your data is **persisted** on your local machine — so you can stop/start the container anytime and your database stays intact.
    

* * *

### 🔹 4. Port Mapping: `-p`

`-p 5432:5432`

*   Maps **port 5432** on your host machine → **port 5432** inside the container.
    
*   Postgres listens on 5432 by default.
    

✅ This means: You can connect to the database from outside Docker (e.g., with `pgcli`, Python, pgAdmin) using:

`host: localhost port: 5432 user: root password: root database: ny_taxi`

* * *

### 🔹 5. Network: `--network=pg-network`

*   Puts this container on a **user-defined Docker network** (named `pg-network`).
    
*   This is crucial if you want **multiple containers to communicate** (e.g., Postgres + pgAdmin).
    

✅ Example: A pgAdmin container on the same `pg-network` can connect using the container name (`pg-database`) instead of `localhost`.

* * *

### 🔹 6. Name: `--name pg-database`

*   Assigns a **custom name** to the container (instead of a random one).
    
*   Easier to reference in commands later, like:
    

`docker exec -it pg-database psql -U root -d ny_taxi`

* * *

### 🔹 7. Image: `postgres:13`

*   Specifies which Docker image to use.
    
*   Here, it pulls and runs **PostgreSQL version 13**.
    

* * *

## 🧠 Summary (What This Command Does)

✅ In one go, this command:

*   Spins up a PostgreSQL 13 database container.
    
*   Creates a user (`root`), password (`root`), and database (`ny_taxi`).
    
*   Persists the data locally (`ny_taxi_postgres_data` folder).
    
*   Exposes it on port 5432 so Python/pgcli can connect.
    
*   Joins it to a Docker network (`pg-network`) so other containers (like pgAdmin) can access it.
    
*   Names the container `pg-database` for easy reference.
    

* * *

### 🔍 Quick Check After Running

Once it’s running, you can verify with:

`docker ps`

You should see something like:

`CONTAINER ID   IMAGE          COMMAND                  STATUS          PORTS                    NAMES abcd1234       postgres:13    "docker-entrypoint.s…"   Up 20 seconds   0.0.0.0:5432->5432/tcp   pg-database`

✅ You’re now ready to connect with:

`pgcli -h localhost -p 5432 -u root -d ny_taxi`

* * *

💡 **Pro Tip:** You only need to run this command **once**. After that, you can stop/start the container any time with:

`docker stop pg-database docker start pg-database`
