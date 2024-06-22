stone_endurance = [1, 2, 1, 4]
dog_list = [
    {
        "이름": "루비독",
        "나이": "95년생",
        "점프력": "3",
        "몸무게": "4",
    },
    {
        "이름": "피치독",
        "나이": "95년생",
        "점프력": "3",
        "몸무게": "3",
    },
    {
        "이름": "씨-독",
        "나이": "72년생",
        "점프력": "2",
        "몸무게": "1",
    },
    {
        "이름": "코볼독",
        "나이": "59년생",
        "점프력": "1",
        "몸무게": "1",
    },
]


def resolve(stone_endurance, dog_list):
    result = [dog_list[dog]["이름"] for dog in range(len(dog_list))]
    # dog_name_list = [i["이름"] for i in dogs]

    for dog in dog_list:
        location = 0
        # index는 0부터 시작하므로, 점프를 2만큼 뛰었다면, 도착한 돌의 index는 0, 1 -> 1이 된다.
        while location < len(stone_endurance) - 1:
            location += int(dog["점프력"])
            stone_endurance[location - 1] -= int(dog["몸무게"])
            if stone_endurance[location - 1] < 0:
                # ex)  result.index('루비독') -> 0
                # result[result.index(dog["이름"])] = "fail"
                del result[result.index(dog["이름"])]
                break
    return [i for i in result if i != "fail"]


print(resolve(stone_endurance, dog_list))
