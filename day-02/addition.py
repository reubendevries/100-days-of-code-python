import sentry_sdk
sentry_sdk.init(
    dsn="https://ed033df89a8c453f80021923b201695b@o4504317994205184.ingest.sentry.io/4504318009409536",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

two_digit_number = input('Type a two digit number:\n')

def additition(s):
    for i in range(len(s)-1):
        return int(s[i]) + int(s[i+1])

if __name__ == '__main__':
    ans = additition(two_digit_number)
    print(ans)