def calculate_revenue_growth(current_revenue, previous_revenue):
    if previous_revenue == 0:
        return None  # Avoid division by zero
    return ((current_revenue - previous_revenue) / previous_revenue) * 100

def calculate_gross_margin(revenue, cogs):
    if revenue == 0:
        return None  # Avoid division by zero
    return ((revenue - cogs) / revenue) * 100

def calculate_ebitda_margin(ebitda, revenue):
    if revenue == 0:
        return None  # Avoid division by zero
    return (ebitda / revenue) * 100

def calculate_burn_rate(monthly_expenses, monthly_revenue):
    return monthly_expenses - monthly_revenue

def calculate_cash_runway(available_cash, monthly_net_burn):
    if monthly_net_burn <= 0:
        return float('inf')  # Infinite runway if burn is zero or negative
    return available_cash / monthly_net_burn

def calculate_customer_acquisition_cost(total_marketing_expenses, new_customers):
    if new_customers == 0:
        return None  # Avoid division by zero
    return total_marketing_expenses / new_customers

def calculate_lifetime_value(avg_revenue_per_user, avg_customer_lifespan):
    return avg_revenue_per_user * avg_customer_lifespan

def calculate_revenue_concentration(revenue_from_top_customers, total_revenue):
    if total_revenue == 0:
        return None  # Avoid division by zero
    return (revenue_from_top_customers / total_revenue) * 100

def calculate_break_even_point(fixed_costs, price_per_unit, variable_costs_per_unit):
    if price_per_unit <= variable_costs_per_unit:
        return None  # No break-even point if price is less than or equal to variable costs
    return fixed_costs / (price_per_unit - variable_costs_per_unit)