def do_stuff(num):
    # print(__name__)
    try:
        return int(num) + 5
    except ValueError as err:
        return err
    except ZeroDivisionError as err:
        return  err
    except TypeError as err:
        return err


