# Use the Plot struct as it is provided
defmodule Plot do
  @enforce_keys [:plot_id, :registered_to]
  defstruct [:plot_id, :registered_to]
end

defmodule CommunityGarden do
  def start(opts \\ []) do
    {:ok, agent_pid} = Agent.start(fn -> %{next_id: 1, plots: []} end)
  end

  def list_registrations(pid) do
    Agent.get(pid, & &1.plots)
  end

  def register(pid, register_to) do
    prev_state = Agent.get_and_update(pid, fn state -> {
      state,
      Map.merge(
        state, 
        %{
          next_id: state.next_id + 1,
          plots: state.plots ++ [%Plot{plot_id: state.next_id, registered_to: register_to}]
        }
      )
    } end)

    %Plot{plot_id: prev_state.next_id, registered_to: register_to}
  end

  def release(pid, plot_id) do
    Agent.update(pid, fn state -> Map.put(state, :plots, Enum.filter(state.plots, & &1.plot_id != plot_id)) end )
  end

  def get_registration(pid, plot_id) do
    Enum.find(Agent.get(pid, & &1.plots), {:not_found, "plot is unregistered"}, & &1.plot_id == plot_id)
  end
end
