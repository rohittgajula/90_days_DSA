import re
import csv
from collections import defaultdict, Counter

# Configure the threshold for suspicious activity detection
FAILED_LOGIN_THRESHOLD = 10

# Parse the log file
def parse_log_file(log_file):
    ip_requests = Counter()
    endpoint_requests = Counter()
    failed_logins = defaultdict(int)

    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*?\] "(?P<method>\w+) (?P<endpoint>/\S*) HTTP/\d\.\d" (?P<status>\d{3})'
    )

    with open(log_file, 'r') as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                ip = match.group('ip')
                endpoint = match.group('endpoint')
                status = int(match.group('status'))

                ip_requests[ip] += 1
                endpoint_requests[endpoint] += 1

                # Detect failed login attempts (status 401)
                if status == 401:
                    failed_logins[ip] += 1

    return ip_requests, endpoint_requests, failed_logins


# Generate analysis results
def generate_results(ip_requests, endpoint_requests, failed_logins):
    # Sort IP requests by count
    sorted_ip_requests = ip_requests.most_common()

    # Identify the most frequently accessed endpoint
    most_accessed_endpoint, access_count = endpoint_requests.most_common(1)[0]

    # Identify suspicious activity
    suspicious_ips = {ip: count for ip, count in failed_logins.items() if count > FAILED_LOGIN_THRESHOLD}

    return sorted_ip_requests, (most_accessed_endpoint, access_count), suspicious_ips


# Save results to CSV
def save_to_csv(ip_requests, most_accessed, suspicious_ips):
    with open('log_analysis_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Write IP requests
        writer.writerow(["IP Address", "Request Count"])
        writer.writerows(ip_requests)

        # Write most accessed endpoint
        writer.writerow([])
        writer.writerow(["Most Accessed Endpoint", "Access Count"])
        writer.writerow([most_accessed[0], most_accessed[1]])

        # Write suspicious activity
        writer.writerow([])
        writer.writerow(["Suspicious Activity", "Failed Login Count"])
        writer.writerows(suspicious_ips.items())


# Display results in the terminal
def display_results(ip_requests, most_accessed, suspicious_ips):
    print("IP Address           Request Count")
    for ip, count in ip_requests:
        print(f"{ip:<20} {count}")

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")

    print("\nSuspicious Activity:")
    if suspicious_ips:
        for ip, count in suspicious_ips.items():
            print(f"{ip:<20} {count}")
    else:
        print("No suspicious activity detected.")


# Main script
def main():
    log_file = "sample.log"  # Update with your log file path
    ip_requests, endpoint_requests, failed_logins = parse_log_file(log_file)
    sorted_ip_requests, most_accessed, suspicious_ips = generate_results(
        ip_requests, endpoint_requests, failed_logins
    )

    display_results(sorted_ip_requests, most_accessed, suspicious_ips)
    save_to_csv(sorted_ip_requests, most_accessed, suspicious_ips)
    print("\nResults saved to log_analysis_results.csv")


if __name__ == "__main__":
    main()
