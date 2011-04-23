import unittest

class Candidate:
    votes = 0

def vote_for(candidate):
    candidate.votes += 1

def get_winners(candidates_list):
    first_winners=[]
    second_winners=[]
    third_winners=[]

    max_vote = 0
    second_max = 0
    third_max = 0

    for can in candidates_list:
        if max_vote < can.votes:
            max_vote = can.votes

    for can in candidates_list:
        if second_max < can.votes and can.votes < max_vote:
            second_max = can.votes

    for can in candidates_list:
        if third_max < can.votes and can.votes < second_max:
            third_max = can.votes

    for can in candidates_list:
        if can.votes == max_vote:
            first_winners.append(can)
        elif can.votes == second_max:
            second_winners.append(can)
        else:
            third_winners.append(can)

    return [first_winners,second_winners,third_winners]

class VotingTestCase(unittest.TestCase):
    def test_when_one_candidate_this_is_the_winner(self):
        john = Candidate()
        vote_for(john)
        self.assertEquals([[john], [], []], get_winners([john]))
    def test_two_candidates_with_same_amount_of_votes_they_win(self):
        john = Candidate()
        alice = Candidate()
        vote_for(john)
        vote_for(alice)
        self.assertEquals([[john, alice], [], []], get_winners([john, alice]))
    def test_two_candidates_with_different_votes(self):
        john = Candidate()
        alice = Candidate()
        vote_for(john)
        vote_for(john)
        vote_for(alice)
        self.assertEquals([[john], [alice], []], get_winners([john,alice]))
    def test_three_candidates(self):
        john = Candidate()
        alice = Candidate()
        bob = Candidate()
        vote_for(john)
        vote_for(john)
        vote_for(bob)
        vote_for(bob)
        vote_for(bob)
        vote_for(alice)
        self.assertEquals([[bob], [john], [alice]], get_winners([john,alice, bob]))


if __name__ == "__main__":
    unittest.main()

