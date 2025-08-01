defmodule TakeANumber do
  def start() do
    spawn(fn -> process() end)
  end

  def process(state \\ 0) do
    receive do
      {:report_state, sender_pid} -> 
        send(sender_pid, state) 
        process(state)
      {:take_a_number, sender_pid} ->
        send(sender_pid, state + 1)
        process(state + 1)
      :stop -> :noop
      _ -> process(state)
    end
  end
end
