# ❓ Doubt–Resolution Journal

A growing document of doubts & answers during my Data Engineering learning journey.  
(Newest doubts are added on top.)

---

## 🆕 Doubt 3  
**Q:** What does `pgcli -h localhost -p 5432 -u root -d ny_taxi` do?  

**Detailed Answer:**  
This command connects to a PostgreSQL database using **pgcli** — a command-line client that’s like `psql`, but with nicer features like syntax highlighting, auto-completion, and table formatting.  

**Breakdown of each part:**  
- **`pgcli`** → The client program you’re running.  
- **`-h localhost`** → `-h` stands for **host**. Here, it tells pgcli to connect to `localhost`, meaning the database server is running on your local machine (in your case, via Docker).  
- **`-p 5432`** → `-p` is the **port number**. Postgres runs by default on port `5432`. When you started the Docker container, you mapped container’s port 5432 to host’s port 5432, so pgcli can reach it.  
- **`-u root`** → `-u` specifies the **username**. In your Docker run command, you set `POSTGRES_USER=root`.  
- **`-d ny_taxi`** → `-d` specifies the **database name**. In your Docker run command, you set `POSTGRES_DB=ny_taxi`.  

**What happens step-by-step:**  
1. `pgcli` tries to connect to Postgres at `localhost:5432`.  
2. It attempts to log in as the user `root`.  
3. It opens the database called `ny_taxi`.  
4. You’ll be asked for the password (in your case, `root`).  
5. If successful, you see a prompt like:  

ny_taxi>

pgsql
Copy code

From here, you can write SQL queries directly inside pgcli.  

**Example usage:**  
```sql
SELECT COUNT(*) FROM yellow_taxi_data;
Takeaway:
This command = Connect me to my Postgres DB (ny_taxi) running on localhost (port 5432) as user root using pgcli.
