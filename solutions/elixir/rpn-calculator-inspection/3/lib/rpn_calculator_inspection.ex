defmodule RPNCalculatorInspection do
  def start_reliability_check(calculator, input) do
    %{input: input, pid: spawn_link(fn -> calculator.(input) end)}
  end

  def await_reliability_check_result(%{pid: pid, input: input}, results) do
    receive do
      {:EXIT, ^pid, :normal} -> Map.put(results, input, :ok)
      {:EXIT, ^pid, _reason} -> Map.put(results, input, :error)
    after
      100 -> Map.put(results, input, :timeout)
    end
  end

  def reliability_check(_calculator, []), do: %{}
  def reliability_check(calculator, inputs) do
    initial_trap_exit_value = Keyword.get(Process.info(self()), :trap_exit)
    
    Process.flag(:trap_exit, true)
    
    reliability_check_results = Enum.map(inputs, &(start_reliability_check(calculator, &1)))
    |> Enum.reduce(%{}, fn pmap, results -> await_reliability_check_result(pmap, results) end)
    
    Process.flag(:trap_exit, initial_trap_exit_value)

    reliability_check_results
  end

  def correctness_check(_calculator, []), do: []
  def correctness_check(calculator, inputs) do   
    Enum.map(inputs, fn input -> Task.async(fn -> calculator.(input) end) end) 
    |> Enum.map(fn task -> Task.await(task, 100) end)
  end
end
