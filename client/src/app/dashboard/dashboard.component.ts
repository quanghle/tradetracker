import { Component, OnInit } from '@angular/core';
import { Apollo, QueryRef } from 'apollo-angular';
import gql from 'graphql-tag';

const TRADES_QUERY = gql`
  query trades {
    trades {
      id
      ticker {
        id
        symbol
      }
      action
      tradeClass
      quantity
      price
      exchange {
        id
        name
      }
      createdDate
      lastModifiedDate
    }
  }
`;

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  trades: any[] = [];
  private query: QueryRef<any>;

  constructor(private apollo: Apollo) { }

  displayedColumns: string[] = ['ticker', 'quantity', 'price', 'type', 'action', 'exchange', 'date'];

  ngOnInit(): void {
    this.query = this.apollo.watchQuery({
      query: TRADES_QUERY
    });

    this.query.valueChanges.subscribe(result => {
      this.trades = result.data && result.data.trades;
      console.log(this.trades)
    });
  }

}
