#! python3

from datetime import datetime, date, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash
from Restaurants import Restaurant, Order, OrderStatus

# Predefined restaurant
BagBite = Restaurant("BagBite")
my_order = Order("John", ["Burger", "Fries"], BagBite.get_items())
my_order1 = Order("Sindre")
my_order1.add_item("Pizza", BagBite.get_items())
BagBite.add_order(my_order)
BagBite.add_order(my_order1)
my_order1.set_status(OrderStatus.IN_PROGRESS)
my_order2 = Order("Peder", ["Shake", "Salad"], BagBite.get_items())
BagBite.add_order(my_order2)

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def home():
    return render_template('home.html', restaurant=BagBite)

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        order_number = int(request.form['order_number'])
        status = request.form['status']
        try:
            BagBite.get_order(order_number).set_status(OrderStatus[status])
        except ValueError as e:
            flash(str(e))
        return redirect(url_for('orders'))

    orders = BagBite.get_orders()
    return render_template('orders.html', orders=orders, OrderStatus=OrderStatus)

@app.route('/opening_hours', methods=['GET', 'POST'])
def opening_hours():
    if request.method == 'POST':
        week_number = int(request.form['week_number'])
        opening_hours = get_opening_hours_for_week(week_number)
    else:
        today = datetime.today()
        week_number = today.isocalendar()[1]
        opening_hours = get_opening_hours_for_week(week_number)

    return render_template('opening_hours.html', week_number=week_number, opening_hours=opening_hours)

def get_opening_hours_for_week(week_number):
    # Get the first day of the week
    year = datetime.today().year
    d = date(year, 1, 1)
    if(d.weekday() > 3):
        d = d + timedelta(7-d.weekday())
    else:
        d = d - timedelta(d.weekday())
    dlt = timedelta(days = (week_number-1)*7)
    # Get the opening hours for each day of the week
    opening_hours = []
    for i in range(7):
        day = d + dlt + timedelta(days=i)
        if day in BagBite.get_open_dates():
            hours = BagBite.get_opening_hours_date(day)
        else:
            hours = None
        opening_hours.append((day, hours))
    return opening_hours


@app.route('/change_opening_hours', methods=['POST'])
def change_opening_hours():
    day_str = datetime.strptime(request.form['day'], '%Y-%m-%d')
    day = date(day_str.year, day_str.month, day_str.day)
    week_number = int(request.form['week_number'])
    opening_time = datetime.strptime(request.form['opening_time'], '%H:%M')
    closing_time = datetime.strptime(request.form['closing_time'], '%H:%M')

    # Change the opening hours for the specified day
    BagBite.set_opening_hours(day, opening_time, closing_time)
    opening_hours = get_opening_hours_for_week(week_number)
    return render_template('opening_hours.html', week_number=week_number, opening_hours=opening_hours)

@app.route('/statistics')
def statistics():
    avg_open_hours_week = BagBite.avg_open_hours_week()
    avg_orders_per_day = BagBite.avg_orders_per_day()
    return render_template('statistics.html', avg_open_hours_week=avg_open_hours_week, avg_orders_per_day=avg_orders_per_day)

if __name__ == '__main__':
    app.run(debug=True)