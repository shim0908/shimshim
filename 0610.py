# TIL
# # def solution(nums):
#     answer = 0
#     return answer

def solution(nums):
    # 고유한 폰켓몬 종류의 수를 센다.
    unique_pokemon_count = len(set(nums))
    
    # 선택할 수 있는 최대 폰켓몬 수는 N/2 이다.
    max_pokemon_to_select = len(nums) // 2
    
    # 두 값 중 작은 값을 반환한다.
    return min(unique_pokemon_count, max_pokemon_to_select)

# 예제 테스트
nums = [3, 1, 2, 3]
print(solution(nums))  # 예상 결과: 2

