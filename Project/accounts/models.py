from common.utils import JsonSerializable
from sql.db import DB


class Account(JsonSerializable):
    def __init__(self, id = -1, balance = 0):
        self.id = id
        self.balance = balance
    def add_points(self, change = 0, from_acct = -1, transaction_type="", memo = ""):
        return self.__change_points(from_acct, self.id, change, transaction_type, memo)
    def remove_points(self, change = 0, to_acct = -1, transaction_type="", memo=""):
        return self.__change_points(self.id, to_acct, change, transaction_type, memo)
    def __change_points(self, account_src, account_dest, change, transaction_type, memo):
        DB.getDB().autocommit = False
        if change > 0:
            # first of the pair should be negative
            change *= -1
        query = """
        INSERT INTO FROM IS601_Bank_Transaction
        (account_src, account_dest, balance_change, transaction_type, memo) VALUES
        (%s, %s, %s, %s, %s)
        """
        pairs = []
        pairs.append((account_src, account_dest, change, transaction_type, memo))
        pairs.append((account_dest, account_src, change * -1, transaction_type, memo))
        try:
            result = DB.insertMany(query, pairs)
            if result.status:
                print("Recored transations pairs", account_src, account_src, change, transaction_type, memo)
                if self.__update_balance():
                    DB.getDB().commit()
                    return True
        except Exception as e:
            print("Error recording point history", e)
            DB.getDB().rollback()
        return False
    def __update_balance(self):
        from sql.db import DB
        try:
            result = DB.update("""
            UPDATE IS601_S_Accounts set balance = 
            (SELECT IFNULL(SUM(balance_change), 0) FROM IS601_Bank_Transaction WHERE account_src = %(acct)s)
            WHERE id = %(acct)s
            """, {"acct":int(self.id)})
            if result.status:
                result = DB.selectOne("SELECT balance FROM IS601_S_Accounts WHERE id = %s", self.id)
                if result.status and result.row:
                    self.balance = result.row["balance"]
                    from flask import session
                    from flask_login import current_user
                    session["user"] = current_user.toJson()
                    return True
        except Exception as e:
            print("Error updating balance", e)
            DB.getDB().rollback()
        return False