def formatDecimal(x: object) -> object:
    try:
        x = ('%f' % x).rstrip('0').rstrip('.')
        return x
    except TypeError:
        return x


def formatInt(x: object) -> object:
    if x == 1:
        x = ''
    elif x == -1:
        x = '-'
    return x


def slopeLinear(x1, y1, x2, y2):
    Formatting = True
    Verify = True
    # Linear Sequences:
    # Solve for slope via point-slope form
    # Solve for y-intercept by substistute in x and y values

    '#Preliminaries'
    if y2 == y1:
        print(f'Zero Slope; \n'
              f'y-intercept = {y1}')
        quit()
    if x2 == x1:
        print('Undefined Slope')
        quit()

    '#Find the slope'
    m = 0
    a = x1 - x2
    b = y1 - y2
    if a != 0:
        m = b / a

    '#Find the y-intercept'
    y_intercept = -m * x1 + y1

    '#Format and/or print'
    if Formatting:
        if y_intercept == 0:
            print(f'y = {formatDecimal(formatInt(m))}x')

        else:
            if y_intercept < 0:
                print(f'y = {formatDecimal(formatInt(m))}x - {formatDecimal(formatInt(y_intercept))}')
            else:
                print(f'y = {formatDecimal(formatInt(m))}x + {formatDecimal(formatInt(y_intercept))}')
    else:
        print(f'y = {m}x + {b}')

    '#Verify'
    if Verify:
        if y2 == m * x2 + y_intercept:
            print('Verified')
        else:
            print('Cannot Verified')


slopeLinear(9, -2, 8, 4)
