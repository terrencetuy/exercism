defmodule TakeANumber do
  def start() do
    spawn(fn -> process() end)
  end

  defp process(state \\ 0) do
    receive do
      {:report_state, sender_pid} -> 
        send(sender_pid, state) 
        process(state)
      {:take_a_number, sender_pid} ->
        state = state + 1
        send(sender_pid, state)
        process(state)
      :stop -> :noop
      _ -> process(state)
    end
  end
end
