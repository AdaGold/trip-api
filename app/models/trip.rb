class Trip < ApplicationRecord
  CONTINENTS = ["Africa", "Antarctica", "Asia", "Australasia", "Europe", "North America", "South America"]
  has_many :trip_reservations, dependent: :destroy

  validates :name, presence: true, uniqueness: true
  validates :continent, presence: true, inclusion: {in: CONTINENTS}
  validates :category, presence: true
  validates :weeks, presence: true, numericality: {greater_than: 0}
  validates :cost, presence: true, numericality: {greater_than: 0}
end
