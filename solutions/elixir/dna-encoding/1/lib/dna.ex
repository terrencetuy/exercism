defmodule DNA do
  def encode_nucleotide(?A), do: 0b0001
  def encode_nucleotide(?C), do: 0b0010
  def encode_nucleotide(?G), do: 0b0100
  def encode_nucleotide(?T), do: 0b1000
  def encode_nucleotide(?\s), do: 0b0000

  def decode_nucleotide(0b0001), do: ?A
  def decode_nucleotide(0b0010), do: ?C
  def decode_nucleotide(0b0100), do: ?G
  def decode_nucleotide(0b1000), do: ?T
  def decode_nucleotide(0b0000), do: ?\s


  def encode(dna) do
    do_encode(dna, <<>>)
  end

  defp do_encode([], encoded), do: encoded

  defp do_encode([first | rest], encoded) do
    encoded = << encoded:: bitstring, encode_nucleotide(first)::4 >>
    do_encode(rest, encoded)
  end

  def decode(dna) do
    do_decode(dna, [])
  end

  defp do_decode(<<>>, decoded), do: reverse(decoded)

  defp do_decode(<<first::4, rest::bitstring>>, decoded) do
    decoded = [decode_nucleotide(first) | decoded]
    do_decode(rest, decoded)
  end

  defp reverse(list), do: do_reverse(list, '')

  defp do_reverse([], reversed), do: reversed
  defp do_reverse([first | rest], reversed), do: do_reverse(rest, [first | reversed])

end