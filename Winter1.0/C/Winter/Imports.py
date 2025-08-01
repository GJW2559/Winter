def give_imports():
    
    try:
        import cnd
        import notepad
        import oobe
        import Users
        import C
    except ImportError:
        try:
            import cnd
        except:
            return "cnd"
        try:
            import notepad
        except:
            return "notepad"
        try:
            import oobe
        except:
            return "oobe"
        try:
            import oobe
        except:
            import Users
        try:
            import C
        except:
            return "Users"
    else:
        return "OK"