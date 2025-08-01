defmodule FreelancerRates do
  @hours_in_day 8.0
  @billable_days_in_month 22

  def daily_rate(hourly_rate) do
    @hours_in_day * hourly_rate
  end

  def apply_discount(before_discount, discount) do
    before_discount * (100 - discount) / 100
  end

  def monthly_rate(hourly_rate, discount) do
    daily_rate(hourly_rate) * @billable_days_in_month
    |> apply_discount(discount)
    |> Float.ceil()
    |> trunc()
  end

  def days_in_budget(budget, hourly_rate, discount) do
    (budget/monthly_rate(hourly_rate, discount)) * @billable_days_in_month
    |> Float.floor(1)
  end

end
