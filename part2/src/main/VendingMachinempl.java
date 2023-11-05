package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {

  private static VendingMachineImpl instance;
  private Map<String, Drink> drinks;
  private int insertedAmount;

  private VendingMachineImpl() {
    drinks = new HashMap<>();
    drinks.put("ScottCola", new Drink("ScottCola", 75, true));
    drinks.put("KarenTea", new Drink("KarenTea", 100, false));
  }

  public static VendingMachineImpl getInstance() {
    if (instance == null) {
      instance = new VendingMachineImpl();
    }
    return instance;
  }

  @Override
  public void insertQuarter() {
    insertedAmount += 25;
  }

  @Override
  public Drink pressButton(String drinkName) throws NotEnoughMoneyException, UnknownDrinkException {
    Drink drink = drinks.get(drinkName);
    if (drink == null) {
      throw new UnknownDrinkException("Unknown drink: " + drinkName);
    }

    if (insertedAmount < drink.getPrice()) {
      throw new NotEnoughMoneyException("Not enough money for " + drinkName);
    }

    insertedAmount = 0;
    return drink;
  }
}
