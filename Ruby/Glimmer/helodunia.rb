
require 'shoes'

include Shoes 

window('Halo Dunia', 300, 150) do
  button('Klik Saya') do
    on_clicked do
      puts 'Tombol telah diklik!'
    end
  end
end.show
