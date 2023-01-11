#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bemtevi.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

    
    
    .pady {
/*   white-space: nowrap; */
  overflow:hidden;
  height:200px;
  width: 700px;
  background-color : blue;
  border-radius:10px;
  color:white
}


.pady:hover {
  height:auto;
  width: 790px;
  color:lightgray
}


.btn {
    display: block;
    text-transform: uppercase;

    font-size: 11px;
    color: #fff;
    width:5px;

    margin: 0 px;
    padding: 10px;

    border: 2px solid #5fe36a;

    overflow: hidden;

    position: relative;

}

.btn::before {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);

    width: 100%;
    height: 100%;

    background-color: #5fe36a;

    z-index: -1;

    transition: .4s ease;

}
.btn::before {
    width: 110%;
    height: 0;
    border-radius: 80%;
}

.btn:hover::before {
    height: 350%;
}



.sombra{
  width:400px;
    height:400px;
 background: linear-gradient(360deg, #000000 -7.34%, rgba(0, 0, 0, 0.82) 25.04%, rgba(196, 196, 196, 0) 97.18%);
}
