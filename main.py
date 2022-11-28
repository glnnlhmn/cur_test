from con_not_closed import con_not_closed, con_not_closed_2
from with_cur_not_closed import with_cur_not_closed
from cur_closed import cur_closed
from cur_not_closed import cur_not_closed


if __name__ == '__main__':
    # The correct way
    cur_closed()

    # Cursor not close (Connection Closed)
    cur_not_closed()

    # Both cursor and connection left open (Check before leaving module)
    con_not_closed_2()

    # Both cursor and connection left open
    con_not_closed()

    # Using a with statement and not closing connection
    with_cur_not_closed()
    print("done")

