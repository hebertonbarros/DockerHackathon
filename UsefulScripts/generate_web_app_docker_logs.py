# Include your modules to import here
import random
import time
import datetime


# Sample log templates to use
access_log_template = '{} INFO GET /{} Status code: " {}'            # Application logs
app_log_template = '{} {} {}'                                    # Application logs
db_log_template = '{} DEBUG Executed SQL query: {}'              # Database debugging logs
container_log_template = '{} INFO container {}'                  # Docker container logs
security_log_template = '{} {} {}'                               # Security logs
session_log_template = '{} INFO User session started: {}'        # Session management log
api_request_log_template = '{} INFO API request: {} {}'          # API request logs 
api_response_log_template = '{} {} API response: {} {}'          # API request logs  
file_upload_log_template = '{} INFO User uploaded file: {}'        # File upload/download logs
file_download_log_template = '{} INFO User downloaded file: {}'    # File upload/download logs
critical_error_log_template = '{} CRITICAL Critical Error: {}'   # Error handling
successful_login_log_template = '{} INFO User {} successfully logged in.'               # Authentication
failed_login_log_template = '{} WARNING Failed login attempt for user {} from IP {}.'   # Authentication
performance_cpu_log_template = '{} PERFORMANCE CPU usage: {}%'                          # Performance metrics logs
performance_memory_log_template = '{} PERFORMANCE Memory usage: {}%'                    # Performance metrics logs
performance_request_time_log_template = '{} PERFORMANCE Request processing time: {}ms'  # Performance metrics logs
cache_hit_log_template = '{} INFO Cache hit for key: {}'                                # Cache logs
cache_miss_log_template = '{} INFO Cache miss for key: {}'                              # Cache logs
email_sent_log_template = '{} INFO Email sent to {} with subject: {}'                   # Notification logs
email_delivery_failed_log_template = '{} ERROR Email delivery failed for message ID: {}'# Notification logs

# New log templates to use related to ERRORs
db_error_log_template = '{} ERROR Database error: {}'                                   # Database error log
auth_error_log_template = '{} ERROR Authentication failed for user: {}'                 # Authentication error log
authz_error_log_template = '{} ERROR Authorization error: {}'                           # Authorization error log
upload_error_log_template = '{} ERROR File upload failed: {}'                           # File upload error log
download_error_log_template = '{} ERROR File download failed: {}'                       # File download error log
api_error_log_template = '{} ERROR API request failed: {}'                              # API error log
session_error_log_template = '{} ERROR Session error: {}'                               # Session error log
app_error_log_template = '{} ERROR Application error: {}'                               # General application error log



# Sample data for generating random logs
ip_addresses = [
    '192.168.1.1',
    '192.168.1.2',
    '192.168.1.3',
    '192.168.1.4',
    '192.168.1.5',
    '192.168.1.6',
    '192.168.1.7',
    '192.168.1.8',
    '192.168.1.9',
    '192.168.2.1',
    '192.168.2.2',
    '192.168.2.3',
    '192.168.2.4',
    '192.168.2.5',
    '192.168.2.6',
    '192.168.2.7',
    '192.168.2.8',
    '192.168.2.9',
    '192.168.3.1',
    '192.168.3.2',
    '192.168.3.3',
    '192.168.3.4',
    '192.168.3.5',
    '192.168.3.6',
    '192.168.3.7',
    '192.168.3.8',
    '192.168.3.9',
    '192.168.4.1',
    '192.168.4.2',
    '192.168.4.3',
    '192.168.4.4',
    '192.168.4.5',
    '192.168.4.6',
    '192.168.4.7',
    '192.168.4.8',
    '192.168.4.9',
    '192.168.5.1',
    '192.168.5.2',
    '192.168.5.3',
    '192.168.5.4',
    '192.168.5.5',
    '192.168.5.6',
    '192.168.5.7',
    '192.168.5.8',
    '192.168.5.9']

usernames = [
    'CoolCrafter47',
    'MidnightHawk',
    'StarGazer23',
    'QuantumCoder',
    'DreamWeaver89',
    'TechNinja007',
    'LunaExplorer',
    'MountainHiker',
    'CodeWarrior42',
    'OceanSurfer15',
    'SnowboarderPro',
    'JazzPianist76',
    'CoffeeAddict28',
    'AdventureSeeker',
    'SoccerChamp11',
    'ScienceGeek99',
    'BookwormMaster',
    'MusicLover71',
    'ArtisticSoul22',
    'MovieBuff44',
    'Beachcomber17',
    'FoodieExplorer',
    'TravelJunkie33',
    'GuitarHero55',
    'NatureLover13',
    'FitnessFreak101',
    'Fashionista78',
    'PetLover26',
    'DIYEnthusiast',
    'SpaceExplorer65',
    'ChefExtraordinaire',
    'YogaMaster49',
    'HistoryBuff88',
    'WildlifeWatcher',
    'AnimeFanatic20',
    'PhotographyPro',
    'StarWarsFan33',
    'CraftyCreator74',
    'DanceDiva19',
    'CarEnthusiast07',
    'GamingWizard66',
    'MovieDirectorX',
    'SoccerStar25',
    'RockClimber77',
    'CyclistAdventures',
    'ScienceFictionFan',
    'Potterhead123',
    'GardeningGuru55',
    'RunningManiac89',
    'TechGoddess007']

http_methods = ['GET',
                'POST',
                'PUT',
                'DELETE',
                'PATCH',
                'HEAD',
                'OPTIONS',
                'CONNECT']

routes = ['index.html', 
          'login', 
          'images/logo.png', 
          'api/data',
          '/admin',
          '/about',
          '/contact',
          '/user/<username>',
          '/blog/<post_id>',
          '/search?q=<query>',
          '/products',
          '/add-to-cart/<product_id>',
          '/checkout',
          '/admin/dashboard',
          '/api/data',
          '/not-found',
          '/view1.html']

response_codes = [200, 301, 302, 304, 401, 403, 404, 500]

http_statuses = ['INFO', 'ERROR', 'DEBUG', 'WARNING', 'CUSTOM']

sql_queries = ['SELECT * FROM users WHERE username=\'john_doe\'',
               'UPDATE products SET price=20 WHERE id=\'1\'', 
               'SELECT * FROM products WHERE product_id=\'1001\'',
               'SELECT DISTINCT users.user_id, users.username FROM users INNER JOIN prices ON users.user_id = prices.user_id',
               'SELECT * FROM prices',
               'SELECT product_name, MAX(price) AS max_price FROM products INNER JOIN prices ON products.product_id = prices.product_id',
               'SELECT product_name, price FROM products INNER JOIN prices ON products.product_id = prices.product_id WHERE price < 50']


container_actions = ['started', 'running', 'paused', 'stopped', 'exited', 'upgrading']

web_server_actions = ['Listening on port 80', 
                      'Request to ' +  str(random.choice(routes)) + ' resulted in ' + str(random.choice(response_codes)),
                      'Listening on port 443 (HTTPS)',
                      'Request to ' +  str(random.choice(routes)) + ' resulted in 200 (OK)',
                      'Request to ' +  str(random.choice(routes)) + ' resulted in 401 (Unauthorized)',
                      'Request to ' +  str(random.choice(routes)) + ' resulted in 301 (Redirect)',
                      'Request to ' +  str(random.choice(routes)) + ' resulted in 204 (No content)',
                      'Error 500 (Internal Server Error) while processing request',
                      'Request to ' +  str(random.choice(routes)) + ' received with method POST',
                      'Client IP address ' + str(random.choice(ip_addresses)) + ' blocked due to too many login attempts',
                      'Access to ' +  str(random.choice(routes)) + ' restricted to authorized users',
                      'Request to ' +  str(random.choice(routes)) + ' received from IP address ' + str(random.choice(ip_addresses)),
                      'Access log rotated for the day',
                      'HTTPS certificate successfully renewed',
                      'Request to ' + str(random.choice(routes)) + ' by user SpaceExplorer65']

    
security_events = ['Suspicious activity detected from IP address ' + str(random.choice(ip_addresses))]

email_subjects = [
    'Welcome - Get Started!',
    'Account Activation for Application',
    'Password Reset Request',
    'New Features & Updates',
    'Subscription Renewal',
    'Invoice for [Application]',
    'Feedback Request: Help Us',
    'Join our Team',
    'Security Alert: Unusual Activity',
    'Exclusive Offer: Upgrade Now!!!']


db_errors = ['Connection to database server failed.',
             'Connection timeout while trying to connect to the database.',
             'Connection refused.',
             'Connection refused by peer.',
             'SQL syntax errors.',
             'SQL query execution error: especified table not found.',
             'Constraint violations',
             'Disk or resources errors'
             ]


authz_errors = ['Insufficient privileges for user: ' + str(random.choice(usernames)),
                'Acces defined for user: ' + str(random.choice(usernames)),
                'Invalid API token.'
               ]


api_errors = ['GET /api/data - 404 Not Found.',
              'POST /api/update - 401 Unauthorized.',
              'PUT /api/resource - 500 Internal Server Error.',
              'DELETE /api/delete - 401 Unauthorized.']


session_errors = ['User ' + str(random.choice(usernames)) + ' session expired unexpectedly.', 
                  'Invalid session token received from user ' + str(random.choice(usernames)) + '.',
                  'Session data corrupted for user ADMIN']


app_errors = ['Exception thrown in main application logic.',
              'Runtime error in API endpoint handling.',
              'Unexpected state encountered in the application.']


file_download_errors = ['File \'document.docx\' not found.',
                       'Unauthorized access to file \'report.pdf\'.',
                       'Unable to retrieve file \'presentation.pptx\'.']


file_updaload_errors = ['Error while processing uploaded file \'document.pdf\'.',
                       'File size exceeds the maximum allowed limit.',
                       'Unsupported file format for \'image.png\'.',
                       'The file is corrupted or its format is unsupported.']




# Create a list to store each log entry
log_entries = []


# Generate 35K random log entries
for _ in range(35000): # Use 50 to test
    
    # Generate random data points 
    rand_time = time.strftime('%d/%b/%Y:%H:%M:%S %z', time.localtime())
    rand_ip = random.choice(ip_addresses)
    rand_username = random.choice(usernames)
    rand_http_method = random.choice(http_methods)
    rand_route = random.choice(routes)
    rand_response_code = random.choice(response_codes)
    rand_http_status = random.choice(http_statuses)
    rand_sql_query = random.choice(sql_queries)
    rand_container_action = random.choice(container_actions)
    rand_web_server_action = random.choice(web_server_actions)
    rand_security_event = random.choice(security_events)
    rand_subject = random.choice(email_subjects)
    
    
    rand_custom_message = f'Processing time for API endpoint {random.choice(routes)}: {random.randint(1, 200)}ms'


    log_type = random.choice(['access', 'app', 'db', 'container', 'web_server', 'security', 'custom',
                              'session', 'api_request', 'api_response', 'file_upload', 'file_download',
                              'error', 'critical_error', 'successful_login', 'failed_login',
                              'performance_cpu', 'performance_memory', 'performance_request_time',
                              'cache_hit', 'cache_miss', 'email_sent', 'email_delivery_failed',
                              # New log types added
                              'database_err', 'auth_err', 'authz_err', 'upload_err', 
                              'download_err', 'api_err', 'session_err', 'app'])
    
    if log_type == 'access':
        log_entry = access_log_template.format(rand_time, rand_route, rand_response_code)
    elif log_type == 'app':
        log_entry1 = app_log_template.format(rand_time, rand_http_status, f'User \'{rand_username}\' logged in.')
        log_entry2 = app_log_template.format(rand_time, rand_http_status, f'User \'{rand_username}\' logged out.')
        log_entry = random.choice([log_entry1, log_entry2])
    elif log_type == 'db':
        log_entry = db_log_template.format(rand_time, rand_sql_query)
    elif log_type == 'container':
        log_entry = container_log_template.format(rand_time, rand_container_action)
    elif log_type == 'security':
        log_entry = security_log_template.format(rand_time, rand_http_status, rand_security_event)
    elif log_type == 'session':
        log_entry = session_log_template.format(rand_time, f'{rand_username}')
    elif log_type == 'api_request':
        log_entry = api_request_log_template.format(rand_time, f'{rand_route}', rand_http_method)
    elif log_type == 'api_response':
        log_entry = api_response_log_template.format(rand_time, rand_http_status, f'{rand_route}', rand_response_code)
    elif log_type == 'file_upload':
        log_entry = file_upload_log_template.format(rand_time, f'{rand_route}')
    elif log_type == 'file_download':
        log_entry = file_download_log_template.format(rand_time, f'{rand_route}')
    elif log_type == 'critical_error':
        log_entry = critical_error_log_template.format(rand_time, f'{rand_custom_message}')
    elif log_type == 'successful_login':
        log_entry = successful_login_log_template.format(rand_time, rand_username)
    elif log_type == 'failed_login':
        log_entry = failed_login_log_template.format(rand_time, rand_http_status, rand_username, rand_ip)
    elif log_type == 'performance_cpu':
        log_entry = performance_cpu_log_template.format(rand_time, random.randint(0, 100))
    elif log_type == 'performance_memory':
        log_entry = performance_memory_log_template.format(rand_time, random.randint(0, 100))
    elif log_type == 'performance_request_time':
        log_entry = performance_request_time_log_template.format(rand_time, random.randint(1, 1000))
    elif log_type == 'cache_hit':
        log_entry = cache_hit_log_template.format(rand_time, f'{rand_custom_message}')
    elif log_type == 'cache_miss':
        log_entry = cache_miss_log_template.format(rand_time, f'{rand_custom_message}')
    elif log_type == 'email_sent':
        log_entry = email_sent_log_template.format(rand_time, rand_username, f'{rand_subject}')
    elif log_type == 'email_delivery_failed':
        log_entry = email_delivery_failed_log_template.format(rand_time, random.randint(1, 1000))
    elif log_type == 'database_err':
        log_entry = db_error_log_template.format(rand_time, random.choice(db_errors))
    elif log_type == 'auth_err':
        log_entry = auth_error_log_template.format(rand_time, f'{rand_username}')
    elif log_type == 'authz_err':
        log_entry = authz_error_log_template.format(rand_time, random.choice(authz_errors))
    elif log_type == 'upload_err':
        log_entry = upload_error_log_template.format(rand_time, random.choice(file_updaload_errors)) 
    elif log_type == 'download_err':
        log_entry = download_error_log_template.format(rand_time, random.choice(file_download_errors))
    elif log_type == 'api_err':
        log_entry = api_error_log_template.format(rand_time, random.choice(api_errors))
    elif log_type == 'session_err':
        log_entry = session_error_log_template.format(rand_time, random.choice(session_errors))
    elif log_type == 'app':
        log_entry = app_error_log_template.format(rand_time, random.choice(app_errors))
    

    log_entries.append(log_entry)
    # print(log_entry)
    # print(log_entries)
    




# Create a new log file and write the log entries to it in disk
ext = '.txt'

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S") # Format the date and time as "YYYYMMDDTTTTTT"
path = '../RawData/raw_wadl_' # wadl = web_app_docker_logs

try:
    with open(path + str(formatted_datetime) + ext, "w") as file:
        for log_entry in log_entries:
            file.write(log_entry + "\n")

    print("Log entries have been saved to " + path + str(current_datetime) + ext)

except Exception as e:
    print("An error occurred while writing the log entries to disk:", e)




