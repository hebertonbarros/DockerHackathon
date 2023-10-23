import random
import datetime
import time

class DatabaseContainerLogGenerator:

    def __init__(self):

        self.container_init_msgs = [
            '[INFO] Container runtime has been chosen.',
            '[INFO] Pulling image from registry...',
            '[INFO] Image successfully pulled from registry.',
            '[INFO] Creating container from image...',
            '[INFO] Container created with ID [container_id].',
            '[INFO] Starting container [container_id]...',
            '[INFO] Container [container_id] started.',
            '[INFO] Establishing environment variables...',
            '[INFO] Environment variables set.',
            '[INFO] Exposing ports to the host machine...',
            '[INFO] Ports successfully exposed.'
        ]
        self.initialization_msgs = [
            '[INFO] Initializing database...',
            '[INFO] Loading configuration...',
            '[INFO] Configuration loaded successfully.',
            '[INFO] Database engine started.',
            '[INFO] Restoring previous session state...',
            '[DEBUG] Checking data integrity...',
            '[INFO] Ready to accept connections.'
        ]

        self.query_logs = [
            '[INFO] Executing query on table users.',
            '[INFO] Executing INSERT operation on table data.',
            '[INFO] Executing DELETE operation on table temp.',
            '[INFO] Query executed successfully on table users.',
            '[ERROR] Query execution failed on table data.',
            '[DEBUG] Transaction started.',
            '[INFO] Updating records in table transactions.',
            '[INFO] Committing transaction on table orders.',
            '[WARNING] Long-running transaction detected on table inventory.',
            '[INFO] Rollback transaction on table payments.',
            '[DEBUG] Stored procedure "sp_UpdateInventory" executed.',
            '[INFO] Backing up table records.'
        ]

        self.error_logs = [
            '[ERROR] ERROR: Database connection failed!',
            '[WARNING] WARNING: Slow query detected on table logs.',
            '[ERROR] ERROR: Deadlock encountered on table resources.',
            '[ERROR] ERROR: Failed to backup database.',
            '[CRITICAL] CRITICAL: Data corruption detected in table users!',
            '[ERROR] Insufficient permissions for query on table salaries.',
            '[WARNING] Connection pool limit reached.',
            '[ERROR] Timeout while connecting to external API.',
            '[CRITICAL] Unable to allocate memory for new transactions.',
            '[ERROR] Unexpected disconnection of client ID #2387.'
        ]

        self.health_check_logs = [
            '[INFO] Health check initiated...',
            '[INFO] Database is healthy.',
            '[INFO] Running scheduled maintenance tasks...',
            '[DEBUG] Verifying database consistency...',
            '[INFO] Index optimization completed.',
            '[INFO] Data replication status: Successful.',
            '[WARNING] Data replication delayed for node 3.',
            '[INFO] Automatic failover initiated for standby database.'
        ]

        self.shutdown_msgs = [
            '[INFO] Received termination signal.',
            '[INFO] Shutting down database...',
            '[INFO] Database engine stopped.',
            '[INFO] Closing active connections...',
            '[INFO] Saving session state...',
            '[INFO] Database engine has shut down gracefully.',
            '[CRITICAL] Emergency shutdown initiated!',
            '[WARNING] Unplanned shutdown - potential data loss!'
        ]

    def generate_log(self, phase):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        if phase == "container_init":
            log_message = random.choice(self.container_init_msgs)
        elif phase == "db_init":
            log_message = random.choice(self.initialization_msgs)
        elif phase == "runtime":
            log_categories = [self.query_logs, self.error_logs, self.health_check_logs, self.shutdown_msgs]
            chosen_category = random.choices(log_categories, weights=[70, 10, 10, 10], k=1)[0]
            log_message = random.choice(chosen_category)
        else:
            log_message = '[ERROR] Invalid log phase specified.'

        return f"{timestamp} {log_message}"

def save_log_to_txt(log, filename='database_logs.txt'):
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(log + '\n')

def simulate_container_lifecycle(generator, log_count=35000, filename='database_logs.txt'):
    phases = ["container_init", "db_init", "runtime"]
    
    for phase in phases:
        if phase == "runtime":
            count = log_count - 20
        else:
            count = 10

        for _ in range(count):
            log = generator.generate_log(phase)
            save_log_to_txt(log, filename)
            time.sleep(0.01)

    print(f"Generated {log_count} logs.")

def main():
    generator = DatabaseContainerLogGenerator()
    simulate_container_lifecycle(generator)

if __name__ == "__main__":
    main()
