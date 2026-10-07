file_path = r"d:\Wood's Forked\woodsmen\Assets\Scripts\Networking\WoodsmenLobbyPlayer.cs"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacement = '''            if (isLocalPlayer)
            {
                LocalPlayer = this;
                
                // Get the real EOS Display Name
                string eosName = EpicTransport.EOSSDKComponent.DisplayName;
                if (!string.IsNullOrEmpty(eosName) && eosName != "User") 
                {
                    CmdSetPlayerName(isHost ? eosName + " (Host)" : eosName);
                }
            }'''

new_content = content.replace('            if (isLocalPlayer)\n            {\n                LocalPlayer = this;\n            }', replacement)

if new_content != content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Successfully patched WoodsmenLobbyPlayer.cs')
else:
    print('Could not find target to replace.')
