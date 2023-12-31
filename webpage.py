#! python3

from datetime import datetime, date, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash
from restaurants import OrderStatus


def create_webpage(restaurant) -> Flask:

    app = Flask(__name__)
    app.secret_key = 'secret_key'

    @app.route('/')
    def home():
        return render_template('home.html', restaurant=restaurant)

    @app.route('/orders', methods=['GET', 'POST'])
    def orders():
        if request.method == 'POST':
            order_number = int(request.form['order_number'])
            status = request.form['status']
            try:
                restaurant.get_order(order_number).set_status(OrderStatus[status])
            except ValueError as e:
                flash(str(e))
            return redirect(url_for('orders'))

        orders = restaurant.get_orders()
        return render_template('orders.html', orders=orders, OrderStatus=OrderStatus)

    @app.route('/opening_hours', methods=['GET', 'POST'])
    def opening_hours():
        if request.method == 'POST':
            week_number = int(request.form['week_number'])
            opening_hours = get_opening_hours_for_week(week_number, restaurant)
        else:
            today = datetime.today()
            week_number = today.isocalendar()[1]
            opening_hours = get_opening_hours_for_week(week_number, restaurant)

        return render_template('opening_hours.html', week_number=week_number, opening_hours=opening_hours)

    @app.route('/change_opening_hours', methods=['POST'])
    def change_opening_hours():
        day_str = datetime.strptime(request.form['day'], '%Y-%m-%d')
        day = date(day_str.year, day_str.month, day_str.day)
        week_number = int(request.form['week_number'])
        opening_time = datetime.strptime(request.form['opening_time'], '%H:%M')
        closing_time = datetime.strptime(request.form['closing_time'], '%H:%M')

        # Change the opening hours for the specified day
        restaurant.set_opening_hours(day, opening_time, closing_time)
        opening_hours = get_opening_hours_for_week(week_number, restaurant)
        return render_template('opening_hours.html', week_number=week_number, opening_hours=opening_hours)

    @app.route('/statistics')
    def statistics():
        avg_open_hours_week = restaurant.avg_open_hours_week()
        avg_orders_per_day = restaurant.avg_orders_per_day()
        return render_template('statistics.html', avg_open_hours_week=avg_open_hours_week,
                               avg_orders_per_day=avg_orders_per_day)
    return app


def get_opening_hours_for_week(week_number, restaurant) -> list:
    """Returns a list of all the opening times for a given week this year"""
    # Get the first day of the week
    year = datetime.today().year
    first_day = date(year, 1, 1)
    offset = 7 - first_day.weekday() if first_day.weekday() > 3 else -first_day.weekday()
    first_day_of_week = first_day + timedelta(days=offset) + timedelta(weeks=week_number - 1)
    # Get the opening hours for each day of the week
    opening_hours = []
    for i in range(7):
        day = first_day_of_week + timedelta(days=i)
        if day in restaurant.get_open_dates():
            hours = restaurant.get_opening_hours_date(day)
        else:
            hours = None
        opening_hours.append((day, hours))
    return opening_hours
