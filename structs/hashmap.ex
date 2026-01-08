defmodule SimpleHashMap do
  def new(size \\ 8), do: %{size: size, buckets: List.duplicate([], size)}

  def put(%{size: size, buckets: buckets} = map, key, value) do
    index = :erlang.phash2(key, size)
    bucket = Enum.at(buckets, index)

    new_bucket =
      case Enum.find_index(bucket, fn {k, _} -> k == key end) do
        nil -> [{key, value} | bucket]
        i -> List.replace_at(bucket, i, {key, value})
      end

    %{map | buckets: List.replace_at(buckets, index, new_bucket)}
  end

  def get(%{size: size, buckets: buckets}, key) do
    index = :erlang.phash2(key, size)
    buckets
    |> Enum.at(index)
    |> Enum.find_value(fn
      {k, v} when k == key -> v
      _ -> nil
    end)
  end
end
