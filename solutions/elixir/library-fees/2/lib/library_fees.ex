defmodule LibraryFees do
  @monday 1
  @before_noon_days_later 28
  @not_before_noon_days_later 29

  def datetime_from_string(string), do: NaiveDateTime.from_iso8601!(string)

  def before_noon?(datetime), do: Time.diff(datetime, ~T[12:00:00]) < 0

  def return_date(checkout_datetime) do
    days_later = days_later(checkout_datetime)

    checkout_datetime
    |> NaiveDateTime.add(days_later, :day)
    |> NaiveDateTime.to_date()
  end

  defp days_later(checkout_datetime) do
    if before_noon?(checkout_datetime) do 
      @before_noon_days_later 
    else 
      @not_before_noon_days_later
    end
  end

  def days_late(planned_return_date, actual_return_datetime) do
    days_late = Date.diff(actual_return_datetime, planned_return_date)
    if days_late > 0 do 
      days_late 
    else 
      0 
    end
  end

  def monday?(datetime) do
    datetime
    |> NaiveDateTime.to_date()
    |> Date.day_of_week()
    |> Kernel.==(@monday)
  end

  def calculate_late_fee(checkout, return, rate) do
    return_datetime = datetime_from_string(return)

    checkout
    |> datetime_from_string()
    |> return_date()
    |> days_late(return_datetime)
    |> Kernel.*(rate)
    |> apply_offer(return_datetime)
  end

  defp apply_offer(fee, return_datetime) do
    if monday?(return_datetime) do
      div(fee, 2)
    else
      fee 
    end
  end
end
