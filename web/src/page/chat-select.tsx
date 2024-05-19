import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import MessageIcon from '@mui/icons-material/Message';
import { Link } from 'react-router-dom';

const List = [
  { icon: <MessageIcon />, title: 'Chat DB', description: '', href: '/chat/db/new' },
  { icon: <MessageIcon />, title: 'Chat Excel', description: '', href: '/chat/excel/new' },
  { icon: <MessageIcon />, title: 'Chat Knowledge', description: '', href: '/chat/knowledge/new' },
];
export function ChatSelect() {
  return (
    <>
      <div className="max-w-3xl m-auto">
        <div className="grid grid-cols-2 grid-col-2 gap-4">
          {List.map((item, index) => {
            return (
              <Link to={item.href} key={index}>
                <div className="cursor-pointer">
                  <Card sx={{ "&:hover": { boxShadow: 6 } }} >
                    <CardContent>
                      <div>
                        <div className="flex">
                          <div>{item.icon}</div>
                          <div>{item.title}</div>
                        </div>
                        {item.description}
                      </div>
                    </CardContent>
                  </Card>
                </div>
              </Link>
            );
          })}
        </div>
      </div>
    </>
  );
}
