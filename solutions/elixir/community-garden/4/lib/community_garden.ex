# Use the Plot struct as it is provided
defmodule Plot do
  @enforce_keys [:plot_id, :registered_to]
  defstruct [:plot_id, :registered_to]
end

defmodule CommunityGarden do
  def start(_opts \\ []), do: Agent.start(fn -> %{next_id: 1, plots: []} end)

  def list_registrations(pid), do: Agent.get(pid, & &1.plots)

  def register(pid, register_to) do
    Agent.get_and_update(pid, fn state -> 
      new_plot = %Plot{plot_id: state.next_id, registered_to: register_to}
      {new_plot, Map.merge(state, %{next_id: state.next_id + 1, plots: state.plots ++ [new_plot]})} 
    end)
  end

  def release(pid, plot_id) do
    Agent.update(pid, fn state -> Map.put(state, :plots, Enum.filter(state.plots, & &1.plot_id != plot_id)) end )
  end

  def get_registration(pid, plot_id) do
    Agent.get(pid, fn state -> Enum.find(state.plots,{:not_found, "plot is unregistered"}, & &1.plot_id == plot_id) end)
  end
end
