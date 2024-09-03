import dns.resolver

def check_mx(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return True if mx_records else False
    except dns.resolver.NoAnswer:
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

domain = "gmail.com"
if check_mx(domain):
    print(f"The domain {domain} has MX records.")
else:
    print(f"The domain {domain} does not have MX records.")
