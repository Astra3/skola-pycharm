from typing import Union
import bluetooth


class BluetoothComm:
    def __init__(self):
        """
        Třída pro komunikaci s Bluetooth zařízením vytvořen pomoci tohoto `návodu <https://www.reddit.com/r/raspberry_pi/comments/6nchaj/guide_how_to_establish_bluetooth_serial/?utm_source=share&utm_medium=web2x&context=3>`_
        Příklad použití::
            with BluetoothComm() as comm:
                comm.send_comm("hello")
        """
        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock.bind(("", bluetooth.PORT_ANY))
        self.server_sock.listen(1)

        port = self.server_sock.getsockname()[1]
        # bluetooth.advertise_service(self.server_sock, "Včelí váha")

        print(f"Čekám na spojení, port: {port}")
        self.client_sock, address = self.server_sock.accept()
        print(f"Připojeno: {address}")

    def send_comm(self, text: object):
        """
        Pošle do Bluetooth terminálu text

        :param text: text co se pošle do terminálu
        """
        self.client_sock.send(text)

    def read_comm(self) -> Union[bytes, None]:
        """
        Vyčkává, dokud se do terminálu nezadá nějaký vstup

        :return: vrací zadaný input nebo None
        """
        res = self.client_sock.recv(1024)
        if len(res):
            return res
        else:
            return None

    def close(self):
        """
        Uzavře connection, aktivuje se automaticky při použití s with
        """
        self.client_sock.close()
        self.server_sock.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

