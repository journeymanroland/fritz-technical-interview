# Lucky Dollar Store Coding Challenge
import random

class Raffle(object):

    def __init__(self):
        super(Raffle, self).__init__()
        self.pool = []
        self.cant_win_again = {}
        self.num_drawings = 1

    def record_customer_purchase(self, customer):
        print("- Added new raffle ticket for \"%s\"" % customer)
        self.pool.append(customer)
        return customer

    def draw_winners(self, num_winners):
        # pick winner(s)
        winning_customer = []
        # people ineligible to win aren't put into the pool of possible winners
        temp_pool = list(filter(lambda x: can_win(x, self.cant_win_again), self.pool)) 
        if num_winners <= len(temp_pool):
            while len(winning_customer) < num_winners:
                winner = random.choice(temp_pool)
                if winner not in winning_customer:
                    winning_customer.append(winner)
            return winning_customer
        else:
            return temp_pool

    def run_weekly_raffle(self, num_winners):
        winners = self.draw_winners(num_winners)
        print(winners)
        print("Raffle Drawing %d" % self.num_drawings)

        # same winner can't win in same drawing

        print("- Picking the weekly winner….", end = " ")

        if not winners:
            print("No one :(")
        else:
            for winner in winners:
                print(winner, end = " ")
                self.cant_win_again.update({winner: 4})

        # decrement number of raffles until winner can win again
        for c in self.cant_win_again:
            if self.cant_win_again[c] != 0:
                self.cant_win_again[c] -= 1

        # increment number of drawings 
        self.num_drawings += 1


def can_win(customer, pool):
    num_raffles_before_eligible = pool.get(customer)
    if not num_raffles_before_eligible or num_raffles_before_eligible == 0:
        return True
    else:
        return False


def main():
    raffle = Raffle()
    raffle.record_customer_purchase("Hally")
    raffle.record_customer_purchase("Hally")
    raffle.record_customer_purchase("Hally")
    raffle.record_customer_purchase("Hally")
    raffle.record_customer_purchase("Hally")
    raffle.record_customer_purchase("Hally")
    raffle.record_customer_purchase("Jerry")
    raffle.record_customer_purchase("Bill")
    raffle.record_customer_purchase("Roland")
    raffle.run_weekly_raffle(4)



if __name__ == '__main__':
    main()
