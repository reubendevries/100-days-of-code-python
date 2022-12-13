import sentry_sdk
sentry_sdk.init(
    dsn="https://ed033df89a8c453f80021923b201695b@o4504317994205184.ingest.sentry.io/4504318009409536",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


def band_generator():
    print('Hello, Welcome to our Band Name Generator Application')
    city = input('Please write the name of the city you were raised in:\n')
    pet = input('Please write the name of a pet you had:\n')

    band_name = 'Your Band Name is: ' + city + ' ' + pet

    return band_name


if __name__ == '__main__':
    band_name = band_generator()
    print(band_name)