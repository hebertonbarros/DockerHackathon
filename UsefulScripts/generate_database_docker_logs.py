import random
import datetime

class DatabaseContainerLogGenerator:

    def __init__(self):
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

    def generate_log_timestamp(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    def generate_log(self):
        log_categories = [self.initialization_msgs, self.query_logs, self.error_logs, self.health_check_logs, self.shutdown_msgs]
        chosen_category = random.choices(log_categories, weights=[5, 70, 10, 10, 5], k=1)[0]
        log_message = random.choice(chosen_category)
        return f"{self.generate_log_timestamp()} {log_message}"


def save_log_to_txt(log, filename='database_logs.txt'):
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(log + '\n')


def main():
    generator = DatabaseContainerLogGenerator()
    log_count = 35000 

    for _ in range(log_count):
        log = generator.generate_log()
        #print(log) 
        save_log_to_txt(log)

    print(f"Generated {log_count} logs.")


if __name__ == "__main__":
    main()
